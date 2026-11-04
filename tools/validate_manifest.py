#!/usr/bin/env python3
"""Validate a WHAT IF WORLD production manifest and enforce an optional release gate."""
from pathlib import Path
import argparse
import json
import re
import sys

STATES = {
    "IDEA_CANDIDATE","IDEA_APPROVED","RESEARCH","STORY","PREPRODUCTION",
    "GENERATION","EDITING","QA","RELEASE_APPROVED","PUBLISHED","ARCHIVED",
    "HOLD","REWORK","REJECTED"
}

def validate(data, release_gate=False):
    errors, blockers = [], []
    if not re.fullmatch(r"WW-\d{3,}", str(data.get("production_id", ""))):
        errors.append("production_id must match WW-###")
    if data.get("state") not in STATES:
        errors.append("state is not a recognized production state")

    claims = data.get("claims", [])
    assets = data.get("assets", [])
    shots = data.get("shots", [])
    claim_ids = {c.get("id") for c in claims}
    asset_ids = {a.get("id") for a in assets}

    for c in claims:
        if c.get("critical") and (c.get("status") not in {"SUPPORTED", "QUALIFIED"} or not c.get("source_ids")):
            blockers.append(f"critical claim {c.get('id')} is unresolved or has no source")
    for a in assets:
        if a.get("rights_status") != "CLEARED":
            blockers.append(f"asset {a.get('id')} rights are not CLEARED")
    for s in shots:
        if s.get("duration_seconds", 0) <= 0 or s.get("duration_seconds", 0) > 20:
            errors.append(f"shot {s.get('id')} has invalid duration")
        for aid in s.get("asset_ids", []):
            if aid not in asset_ids:
                errors.append(f"shot {s.get('id')} references unknown asset {aid}")
        for cid in s.get("claim_ids", []):
            if cid not in claim_ids:
                errors.append(f"shot {s.get('id')} references unknown claim {cid}")
        if release_gate and s.get("status") != "APPROVED":
            blockers.append(f"shot {s.get('id')} is not APPROVED")

    if release_gate:
        if data.get("state") not in {"RELEASE_APPROVED", "PUBLISHED", "ARCHIVED"}:
            blockers.append("production state has not reached release approval")
        approval = data.get("approvals", {}).get("release", {})
        if approval.get("status") != "APPROVED" or not approval.get("by") or not approval.get("at"):
            blockers.append("human release approval is missing")
        release = data.get("release", {})
        if not release.get("final_master") or not release.get("sha256"):
            blockers.append("final master path and SHA-256 are required")
        if not release.get("caption") or not release.get("ai_disclosure_checked"):
            blockers.append("caption or AI disclosure check is missing")
        if any(c.get("critical") and c.get("status") not in {"SUPPORTED", "QUALIFIED"} for c in claims):
            pass

    return errors, blockers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--release-gate", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: cannot read JSON manifest: {exc}")
        return 2
    errors, blockers = validate(data, args.release_gate)
    for e in errors:
        print("ERROR:", e)
    for b in blockers:
        print("BLOCKER:", b)
    if errors or (args.release_gate and blockers):
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS" if not blockers else f"FORMAT PASS; {len(blockers)} release blocker(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
