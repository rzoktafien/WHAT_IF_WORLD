#!/usr/bin/env python3
"""Dependency-free structural and cross-reference validation for WHAT IF WORLD manifests."""
from pathlib import Path
import argparse
import json
import re
import sys
from datetime import datetime
from urllib.parse import urlparse

STATES={"IDEA_CANDIDATE","IDEA_APPROVED","RESEARCH","STORY","PREPRODUCTION","PILOT_GENERATION","BATCH_GENERATION","GENERATION","EDITING","QA","RELEASE_APPROVED","PUBLISHED","ARCHIVED","HOLD","REWORK","REJECTED"}
PATTERNS={
 "production":re.compile(r"^WW-[0-9]{3,}$"),"source":re.compile(r"^SRC-[0-9]{3,}$"),
 "claim":re.compile(r"^CLM-[0-9]{3,}$"),"asset":re.compile(r"^AST-[A-Z]+-[0-9]{3,}$"),
 "character":re.compile(r"^AST-CHAR-[0-9]{3,}$"),"shot":re.compile(r"^SH-[0-9]{3,}$"),
 "version":re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")}
CLAIM_STATUSES={"SUPPORTED","QUALIFIED","UNVERIFIED","REJECTED"}
RIGHTS={"CLEARED","NOT_REQUIRED","PENDING","REJECTED"}
CHARACTER_STATUSES={"DRAFT","REVIEW","APPROVED","SUPERSEDED","REJECTED"}
GENERATION_STATES={"PILOT_GENERATION","BATCH_GENERATION","GENERATION","EDITING","QA","RELEASE_APPROVED","PUBLISHED","ARCHIVED"}

def _valid_datetime(value):
    if not isinstance(value,str) or not value.strip(): return False
    try:
        parsed=datetime.fromisoformat(value.replace("Z","+00:00"))
        return parsed.tzinfo is not None and parsed.utcoffset() is not None
    except ValueError:
        return False

def _ids(items,label,pattern,errors):
    seen=set(); found=set()
    for i,item in enumerate(items):
        if not isinstance(item,dict):
            errors.append(f"{label}[{i}] must be an object"); continue
        value=item.get("id")
        if not isinstance(value,str) or not pattern.fullmatch(value):
            errors.append(f"{label}[{i}] has invalid id: {value!r}"); continue
        if value in seen: errors.append(f"duplicate {label} ID: {value}")
        seen.add(value); found.add(value)
    return found


APPROVAL_STATES = {
 "IDEA_APPROVED": ("idea",), "RESEARCH": ("idea",), "STORY": ("idea",), "PREPRODUCTION": ("idea",),
 "PILOT_GENERATION": ("idea",), "BATCH_GENERATION": ("idea", "pilot_generation"),
 "GENERATION": ("idea", "pilot_generation", "batch_generation"),
 "EDITING": ("idea", "pilot_generation", "batch_generation", "generation"),
 "QA": ("idea", "pilot_generation", "batch_generation", "generation", "asset_qa"),
 "RELEASE_APPROVED": ("idea", "pilot_generation", "batch_generation", "generation", "asset_qa", "master_qa", "release"),
 "PUBLISHED": ("idea", "pilot_generation", "batch_generation", "generation", "asset_qa", "master_qa", "release"),
 "ARCHIVED": ("idea", "pilot_generation", "batch_generation", "generation", "asset_qa", "master_qa", "release")
}
def _approval_is_valid(value):
    return (isinstance(value,dict) and value.get("status")=="APPROVED"
            and isinstance(value.get("by"),str) and bool(value.get("by").strip())
            and _valid_datetime(value.get("at")))

def validate(data,release_gate=False):
    errors=[]; blockers=[]
    if not isinstance(data,dict): return ["manifest root must be an object"],[]
    required_manifest_fields=("production_id","version","title","state","pillar","premise","claims","sources","assets","shots","approvals","release")
    for field in required_manifest_fields:
        if field not in data: errors.append(f"manifest is missing required field {field}")
    if not PATTERNS["production"].fullmatch(str(data.get("production_id",""))): errors.append("production_id must match WW-###")
    if not PATTERNS["version"].fullmatch(str(data.get("version",""))): errors.append("manifest version must use semver MAJOR.MINOR.PATCH")
    for field,minimum in (("title",3),("pillar",1),("premise",5)):
        value=data.get(field)
        if not isinstance(value,str) or len(value.strip())<minimum:
            errors.append(f"manifest {field} must be a non-empty string of at least {minimum} characters")
    if data.get("state") not in STATES: errors.append("state is not a recognized production state")
    for field in ("approvals","release"):
        if not isinstance(data.get(field),dict): errors.append(f"manifest {field} must be an object")
    cols={}
    for name in ("sources","claims","assets","character_references","shots"):
        val=data.get(name,[])
        if not isinstance(val,list): errors.append(f"{name} must be an array"); val=[]
        cols[name]=val
    src=_ids(cols["sources"],"sources",PATTERNS["source"],errors)
    for source in cols["sources"]:
        if not isinstance(source,dict): continue
        title=source.get("title")
        if not isinstance(title,str) or len(title.strip())<3:
            errors.append(f"source {source.get('id')} is missing a valid title")
        url=source.get("url")
        parsed=urlparse(url) if isinstance(url,str) else None
        if parsed is None or parsed.scheme not in {"http","https"} or not parsed.netloc:
            errors.append(f"source {source.get('id')} is missing a valid http(s) URL")
    claim_ids=_ids(cols["claims"],"claims",PATTERNS["claim"],errors)
    asset_ids=_ids(cols["assets"],"assets",PATTERNS["asset"],errors)
    asset_by_id={a.get("id"):a for a in cols["assets"] if isinstance(a,dict) and isinstance(a.get("id"),str)}
    char_ids=_ids(cols["character_references"],"character_references",PATTERNS["character"],errors)
    shot_ids=_ids(cols["shots"],"shots",PATTERNS["shot"],errors)
    for duplicate_id in asset_ids & char_ids:
        errors.append(f"asset ID collides with character ID: {duplicate_id}")
    character_by_id={c.get("id"):c for c in cols["character_references"] if isinstance(c,dict) and isinstance(c.get("id"),str)}
    for c in cols["claims"]:
        if not isinstance(c,dict): continue
        claim_text=c.get("claim")
        if not isinstance(claim_text,str) or len(claim_text.strip())<5:
            errors.append(f"claim {c.get('id')} is missing a valid claim statement")
        if c.get("class") not in {"FACT","EXTRAPOLATION","FICTIONAL_ASSUMPTION"}:
            errors.append(f"claim {c.get('id')} has invalid class")
        if c.get("confidence") not in {"HIGH","MEDIUM","LOW"}:
            errors.append(f"claim {c.get('id')} has invalid confidence")
        safe_wording=c.get("safe_wording")
        if not isinstance(safe_wording,str) or len(safe_wording.strip())<5:
            errors.append(f"claim {c.get('id')} is missing valid safe_wording")
        if c.get("critical") is not None and not isinstance(c.get("critical"),bool):
            errors.append(f"claim {c.get('id')} critical must be boolean")
        if c.get("status") not in CLAIM_STATUSES: errors.append(f"claim {c.get('id')} has invalid status")
        refs=c.get("source_ids",[])
        if not isinstance(refs,list): errors.append(f"claim {c.get('id')} source_ids must be an array"); refs=[]
        for sid in refs:
            if sid not in src: errors.append(f"claim {c.get('id')} references unknown source {sid}")
        if c.get("critical") and (c.get("status") not in {"SUPPORTED","QUALIFIED"} or not refs):
            blockers.append(f"critical claim {c.get('id')} is unresolved or has no source")
    for a in cols["assets"]:
        if not isinstance(a,dict): continue
        rights=a.get("rights_status")
        if rights is not None and rights not in RIGHTS: errors.append(f"asset {a.get('id')} has invalid rights_status")
        if release_gate and rights not in {"CLEARED","NOT_REQUIRED"}: blockers.append(f"asset {a.get('id')} rights are not cleared")
    for c in cols["character_references"]:
        if not isinstance(c,dict): continue
        cid=c.get("id"); status=c.get("status"); canonical=c.get("canonical_reference")
        if status not in CHARACTER_STATUSES: errors.append(f"character {cid} has invalid status")
        if not isinstance(c.get("owner"),str) or len(c.get("owner","").strip())<2: errors.append(f"character {cid} is missing owner")
        if not isinstance(c.get("name"),str) or len(c.get("name","").strip())<2: errors.append(f"character {cid} is missing name")
        if c.get("production_id") != data.get("production_id"): errors.append(f"character {cid} belongs to a different production or has no production_id")
        for field in ("created_at","updated_at"):
            if not _valid_datetime(c.get(field)): errors.append(f"character {cid} has invalid {field} date-time")
        identity=c.get("identity")
        if not isinstance(identity,dict):
            errors.append(f"character {cid} is missing identity object")
        else:
            for field in ("face_shape","hair"):
                if not isinstance(identity.get(field),str) or len(identity.get(field,"").strip())<2:
                    errors.append(f"character {cid} identity is missing valid {field}")
            traits=identity.get("invariant_traits")
            if not isinstance(traits,list) or not traits or any(not isinstance(t,str) or len(t.strip())<2 for t in traits):
                errors.append(f"character {cid} identity invariant_traits must be a non-empty array of valid strings")
        wardrobe=c.get("wardrobe_variants")
        if not isinstance(wardrobe,list):
            errors.append(f"character {cid} wardrobe_variants must be an array")
        else:
            for index,variant in enumerate(wardrobe):
                if not isinstance(variant,dict):
                    errors.append(f"character {cid} wardrobe_variants[{index}] must be an object"); continue
                for field in ("variant_id","description"):
                    if not isinstance(variant.get(field),str) or len(variant.get(field,"").strip())<2:
                        errors.append(f"character {cid} wardrobe_variants[{index}] is missing valid {field}")
                applicable=variant.get("applicable_shots",[])
                if not isinstance(applicable,list):
                    errors.append(f"character {cid} wardrobe_variants[{index}] applicable_shots must be an array")
                else:
                    for shot_id in applicable:
                        if shot_id not in shot_ids: errors.append(f"character {cid} wardrobe variant references unknown shot {shot_id}")
        if c.get("rights_status") not in RIGHTS: errors.append(f"character {cid} has invalid or missing rights_status")
        if not isinstance(canonical,dict): errors.append(f"character {cid} has no canonical_reference")
        else:
            for field in ("provenance","creator","source"):
                if not isinstance(canonical.get(field),str) or len(canonical.get(field,"").strip())<2:
                    errors.append(f"character {cid} canonical_reference is missing {field}")
            kind=canonical.get("kind")
            if kind not in {"image","prompt"}: errors.append(f"character {cid} canonical_reference has invalid kind")
            elif kind=="image" and (not isinstance(canonical.get("uri"),str) or not canonical.get("uri","").strip()):
                errors.append(f"character {cid} image canonical_reference is missing uri")
            elif kind=="prompt" and (not isinstance(canonical.get("prompt"),str) or not canonical.get("prompt","").strip()):
                errors.append(f"character {cid} prompt canonical_reference is missing prompt")
            checksum=canonical.get("checksum")
            if checksum is not None and not re.fullmatch(r"[a-fA-F0-9]{64}",str(checksum)):
                errors.append(f"character {cid} canonical_reference checksum must be a SHA-256 hex digest")
        if "linked_shots" not in c or not isinstance(c.get("linked_shots"),list):
            errors.append(f"character {cid} linked_shots must be an array")
        if not PATTERNS["version"].fullmatch(str(c.get("version",""))): errors.append(f"character {cid} has invalid version")
        if status=="APPROVED":
            approval=c.get("approval")
            if not isinstance(approval,dict) or not isinstance(approval.get("by"),str) or not approval.get("by").strip() or not _valid_datetime(approval.get("at")):
                errors.append(f"approved character {cid} is missing approval.by or approval.at (approval.at must be a timezone-aware date-time)")
        linked=c.get("linked_shots",[])
        if not isinstance(linked,list): errors.append(f"character {cid} linked_shots must be an array"); linked=[]
        for shot_id in linked:
            if shot_id not in shot_ids: errors.append(f"character {cid} links unknown shot {shot_id}")
        if release_gate and status!="APPROVED": blockers.append(f"character {cid} is not APPROVED")
        if release_gate and c.get("rights_status") not in {"CLEARED","NOT_REQUIRED"}: blockers.append(f"character {cid} reference rights are unresolved")
    for s in cols["shots"]:
        if not isinstance(s,dict): continue
        sid=s.get("id"); duration=s.get("duration_seconds")
        for field,minimum in (("id",1),("production_id",1),("purpose",5),("start_state",3),("action",3),("camera_move",3),("end_state",3)):
            value=s.get(field)
            if not isinstance(value,str) or len(value.strip())<minimum:
                errors.append(f"shot {sid} is missing valid required field {field}")
        if not isinstance(duration,(int,float)) or isinstance(duration,bool) or not 0<duration<=20: errors.append(f"shot {sid} has invalid duration")
        if s.get("production_id") != data.get("production_id"): errors.append(f"shot {sid} belongs to a different production or has no production_id")
        if s.get("status") not in {"PLANNED","PILOT","GENERATED","SELECTED","REWORK","REJECTED","APPROVED"}:
            errors.append(f"shot {sid} has invalid status")
        asset_refs=s.get("asset_ids",[])
        if not isinstance(asset_refs,list): errors.append(f"shot {sid} asset_ids must be an array"); asset_refs=[]
        for aid in asset_refs:
            if aid not in asset_ids and aid not in char_ids: errors.append(f"shot {sid} references unknown asset {aid}")
        character_refs=s.get("character_ids",[])
        if not isinstance(character_refs,list): errors.append(f"shot {sid} character_ids must be an array"); character_refs=[]
        versions=s.get("character_reference_versions",{})
        if not isinstance(versions,dict): errors.append(f"shot {sid} character_reference_versions must be an object"); versions={}
        for cid in character_refs:
            if cid in char_ids and sid not in character_by_id[cid].get("linked_shots",[]):
                errors.append(f"shot {sid} links character {cid} but character linked_shots does not include the shot")
            if cid not in char_ids:
                errors.append(f"shot {sid} references unknown character {cid}")
            else:
                profile_version=character_by_id[cid].get("version")
                if versions.get(cid)!=profile_version:
                    errors.append(f"shot {sid} has missing or mismatched character reference version for {cid}")
        for cid in versions:
            if cid not in character_refs: errors.append(f"shot {sid} has a version entry for unlinked character {cid}")
        claim_refs=s.get("claim_ids",[])
        if not isinstance(claim_refs,list):
            errors.append(f"shot {sid} claim_ids must be an array"); claim_refs=[]
        for cid in claim_refs:
            if cid not in claim_ids: errors.append(f"shot {sid} references unknown claim {cid}")
        if release_gate and s.get("status")!="APPROVED": blockers.append(f"shot {sid} is not APPROVED")
    for c in cols["character_references"]:
        if not isinstance(c,dict): continue
        cid=c.get("id")
        for shot_id in c.get("linked_shots",[]) if isinstance(c.get("linked_shots",[]),list) else []:
            linked_shot=next((s for s in cols["shots"] if isinstance(s,dict) and s.get("id")==shot_id),None)
            if linked_shot and cid not in linked_shot.get("character_ids",[]):
                errors.append(f"character {cid} linked_shots includes {shot_id} but shot does not link character")
    if data.get("state") in GENERATION_STATES:
        for shot in cols["shots"]:
            if not isinstance(shot,dict): continue
            sid=shot.get("id")
            for cid in shot.get("character_ids",[]) if isinstance(shot.get("character_ids",[]),list) else []:
                character=character_by_id.get(cid)
                if character is None: continue
                if character.get("status")!="APPROVED":
                    blockers.append(f"shot {sid} character {cid} is not APPROVED for generation/edit/release")
                if character.get("rights_status") not in {"CLEARED","NOT_REQUIRED"}:
                    blockers.append(f"shot {sid} character {cid} reference rights are unresolved")
            for aid in shot.get("asset_ids",[]) if isinstance(shot.get("asset_ids",[]),list) else []:
                asset=asset_by_id.get(aid)
                if asset is not None and asset.get("rights_status") not in {"CLEARED","NOT_REQUIRED"}:
                    blockers.append(f"shot {sid} asset {aid} rights are unresolved")
    approvals=data.get("approvals") if isinstance(data.get("approvals"),dict) else {}
    for approval_stage in APPROVAL_STATES.get(data.get("state"),()):
        if not _approval_is_valid(approvals.get(approval_stage)):
            blockers.append(f"human {approval_stage} approval is missing or lacks approver/time evidence")
    if release_gate:
        if data.get("state") not in {"RELEASE_APPROVED","PUBLISHED","ARCHIVED"}: blockers.append("production state has not reached release approval")
        if not _approval_is_valid(approvals.get("release")):
            blockers.append("human release approval is missing or lacks approver/time evidence")
        release=data.get("release") if isinstance(data.get("release"),dict) else {}
        if not release.get("final_master"): blockers.append("final master path is required")
        if not re.fullmatch(r"[a-fA-F0-9]{64}",str(release.get("sha256",""))): blockers.append("final master SHA-256 is missing or invalid")
        if not release.get("caption") or release.get("ai_disclosure_checked") is not True: blockers.append("caption or AI disclosure check is missing")
    return errors,blockers

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest",type=Path); parser.add_argument("--release-gate",action="store_true")
    args=parser.parse_args()
    try: data=json.loads(args.manifest.read_text(encoding="utf-8"))
    except Exception as exc: print(f"FAIL: cannot read JSON manifest: {exc}"); return 2
    errors,blockers=validate(data,args.release_gate)
    for e in errors: print("ERROR:",e)
    for b in blockers: print("BLOCKER:",b)
    stage_gate=data.get("state") in GENERATION_STATES
    if errors or ((args.release_gate or stage_gate) and blockers): print("RESULT: FAIL"); return 1
    print("RESULT: PASS" if not blockers else f"FORMAT PASS; {len(blockers)} release blocker(s)")
    return 0

if __name__=="__main__": sys.exit(main())
