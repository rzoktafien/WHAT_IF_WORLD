#!/usr/bin/env python3
"""Dependency-free structural and cross-reference validation for WHAT IF WORLD manifests."""
from pathlib import Path
import argparse
import json
import re
import sys

STATES={"IDEA_CANDIDATE","IDEA_APPROVED","RESEARCH","STORY","PREPRODUCTION","GENERATION","EDITING","QA","RELEASE_APPROVED","PUBLISHED","ARCHIVED","HOLD","REWORK","REJECTED"}
PATTERNS={
 "production":re.compile(r"^WW-[0-9]{3,}$"),"source":re.compile(r"^SRC-[0-9]{3,}$"),
 "claim":re.compile(r"^CLM-[0-9]{3,}$"),"asset":re.compile(r"^AST-[A-Z]+-[0-9]{3,}$"),
 "character":re.compile(r"^AST-CHAR-[0-9]{3,}$"),"shot":re.compile(r"^SH-[0-9]{3,}$"),
 "version":re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")}
CLAIM_STATUSES={"SUPPORTED","QUALIFIED","UNVERIFIED","REJECTED"}
RIGHTS={"CLEARED","NOT_REQUIRED","PENDING","REJECTED"}
CHARACTER_STATUSES={"DRAFT","REVIEW","APPROVED","SUPERSEDED","REJECTED"}

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

def validate(data,release_gate=False):
    errors=[]; blockers=[]
    if not isinstance(data,dict): return ["manifest root must be an object"],[]
    if not PATTERNS["production"].fullmatch(str(data.get("production_id",""))): errors.append("production_id must match WW-###")
    if data.get("state") not in STATES: errors.append("state is not a recognized production state")
    cols={}
    for name in ("sources","claims","assets","character_references","shots"):
        val=data.get(name,[])
        if not isinstance(val,list): errors.append(f"{name} must be an array"); val=[]
        cols[name]=val
    src=_ids(cols["sources"],"sources",PATTERNS["source"],errors)
    claim_ids=_ids(cols["claims"],"claims",PATTERNS["claim"],errors)
    asset_ids=_ids(cols["assets"],"assets",PATTERNS["asset"],errors)
    char_ids=_ids(cols["character_references"],"character_references",PATTERNS["character"],errors)
    shot_ids=_ids(cols["shots"],"shots",PATTERNS["shot"],errors)
    character_by_id={c.get("id"):c for c in cols["character_references"] if isinstance(c,dict) and isinstance(c.get("id"),str)}
    for c in cols["claims"]:
        if not isinstance(c,dict): continue
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
        if not isinstance(c.get("owner"),str) or not c.get("owner","").strip(): errors.append(f"character {cid} is missing owner")
        for field in ("created_at","updated_at"):
            value=c.get(field)
            if not isinstance(value,str) or not value.strip(): errors.append(f"character {cid} is missing {field}")
        if not isinstance(canonical,dict): errors.append(f"character {cid} has no canonical_reference")
        else:
            for field in ("provenance","creator","source"):
                if not isinstance(canonical.get(field),str) or not canonical.get(field,"").strip():
                    errors.append(f"character {cid} canonical_reference is missing {field}")
        if "linked_shots" not in c or not isinstance(c.get("linked_shots"),list):
            errors.append(f"character {cid} linked_shots must be an array")
        if not PATTERNS["version"].fullmatch(str(c.get("version",""))): errors.append(f"character {cid} has invalid version")
        if status=="APPROVED":
            approval=c.get("approval")
            if not isinstance(approval,dict) or not isinstance(approval.get("by"),str) or not approval.get("by").strip() or not isinstance(approval.get("at"),str) or not approval.get("at").strip():
                errors.append(f"approved character {cid} is missing approval.by or approval.at")
            if not isinstance(canonical,dict): errors.append(f"approved character {cid} has no canonical_reference")
            elif canonical.get("kind")=="image" and not canonical.get("uri"): errors.append(f"approved character {cid} image reference has no uri")
            elif canonical.get("kind")=="prompt" and not canonical.get("prompt"): errors.append(f"approved character {cid} prompt reference has no prompt")
            elif canonical.get("kind") not in {"image","prompt"}: errors.append(f"approved character {cid} has invalid canonical reference kind")
        linked=c.get("linked_shots",[])
        if not isinstance(linked,list): errors.append(f"character {cid} linked_shots must be an array"); linked=[]
        for shot_id in linked:
            if shot_id not in shot_ids: errors.append(f"character {cid} links unknown shot {shot_id}")
        if release_gate and status!="APPROVED": blockers.append(f"character {cid} is not APPROVED")
        if release_gate and c.get("rights_status") not in {"CLEARED","NOT_REQUIRED"}: blockers.append(f"character {cid} reference rights are unresolved")
    for s in cols["shots"]:
        if not isinstance(s,dict): continue
        sid=s.get("id"); duration=s.get("duration_seconds")
        if not isinstance(duration,(int,float)) or isinstance(duration,bool) or not 0<duration<=20: errors.append(f"shot {sid} has invalid duration")
        if s.get("production_id") not in (None,data.get("production_id")): errors.append(f"shot {sid} belongs to a different production")
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
        for cid in s.get("claim_ids",[]):
            if cid not in claim_ids: errors.append(f"shot {sid} references unknown claim {cid}")
        if release_gate and s.get("status")!="APPROVED": blockers.append(f"shot {sid} is not APPROVED")
    for c in cols["character_references"]:
        if not isinstance(c,dict): continue
        cid=c.get("id")
        for shot_id in c.get("linked_shots",[]) if isinstance(c.get("linked_shots",[]),list) else []:
            linked_shot=next((s for s in cols["shots"] if isinstance(s,dict) and s.get("id")==shot_id),None)
            if linked_shot and cid not in linked_shot.get("character_ids",[]):
                errors.append(f"character {cid} linked_shots includes {shot_id} but shot does not link character")
    if release_gate:
        if data.get("state") not in {"RELEASE_APPROVED","PUBLISHED","ARCHIVED"}: blockers.append("production state has not reached release approval")
        approvals=data.get("approvals") if isinstance(data.get("approvals"),dict) else {}
        approval=approvals.get("release",{})
        if not isinstance(approval,dict) or approval.get("status")!="APPROVED" or not approval.get("by") or not approval.get("at"):
            blockers.append("human release approval is missing")
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
    if errors or (args.release_gate and blockers): print("RESULT: FAIL"); return 1
    print("RESULT: PASS" if not blockers else f"FORMAT PASS; {len(blockers)} release blocker(s)")
    return 0

if __name__=="__main__": sys.exit(main())
