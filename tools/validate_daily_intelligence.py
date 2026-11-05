#!/usr/bin/env python3
"""Validate Daily Intelligence provenance and freshness; this does not perform research."""
from pathlib import Path
import argparse, json, sys
from datetime import datetime, timezone
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
SCHEMA_PATH=ROOT/"schemas/daily_intelligence_report.schema.json"
REPORT_DIR=ROOT/"reports/daily-intelligence"
LANES={"EARTH","NATURE & PHYSICS","HUMAN","ECOSYSTEM","CIVILIZATION & TECHNOLOGY"}

def validate_report(data, now=None):
    now=now or datetime.now(timezone.utc)
    schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors=[f"schema: {e.message}" for e in Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(data)]
    if errors: return errors
    run_at=datetime.fromisoformat(data["run_at"].replace("Z","+00:00"))
    age=(now-run_at).total_seconds()
    if age < -86400: errors.append("run_at is more than 24 hours in the future")
    if age > 7*86400: errors.append("report is older than 7 days")
    if data["status"]!="COMPLETED": errors.append("report status is not COMPLETED")
    if data["truncated"]: errors.append("report is materially truncated")
    missing=LANES-set(data["coverage"])
    if missing: errors.append("missing discovery lanes: "+", ".join(sorted(missing)))
    source_ids={s["id"] for s in data["sources"]}
    claim_ids={c["id"] for c in data["claims"]}
    if len(source_ids)!=len(data["sources"]): errors.append("duplicate source IDs")
    if len(claim_ids)!=len(data["claims"]): errors.append("duplicate claim IDs")
    for claim in data["claims"]:
        for sid in claim["source_ids"]:
            if sid not in source_ids: errors.append(f"{claim['id']} references missing source {sid}")
        if claim.get("critical") and (claim["status"] not in {"SUPPORTED","QUALIFIED"} or not claim["source_ids"]):
            errors.append(f"critical claim {claim['id']} is unresolved or unsourced")
    for source in data["sources"]:
        for cid in source["claim_ids"]:
            if cid not in claim_ids: errors.append(f"{source['id']} references missing claim {cid}")
        if source.get("inspection")=="SEARCH_ONLY" and source["source_type"]=="PRIMARY":
            errors.append(f"{source['id']} is marked primary but only search-result evidence was inspected")
    for candidate in data["candidates"]:
        unknown=set(candidate["source_claim_ids"])-claim_ids
        if unknown: errors.append(f"{candidate['id']} references missing claims: {', '.join(sorted(unknown))}")
    if not data["sources"]: errors.append("report contains no traceable sources")
    if not data["claims"]: errors.append("report contains no claim ledger")
    return errors

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report",nargs="?",type=Path)
    parser.add_argument("--latest",action="store_true",help="validate newest JSON report under reports/daily-intelligence")
    args=parser.parse_args()
    if args.latest:
        files=sorted(REPORT_DIR.glob("*.json"),key=lambda p:p.name,reverse=True)
        if not files:
            print("HOLD: no persisted Daily Intelligence JSON report found")
            return 1
        path=files[0]
    elif args.report: path=args.report
    else: parser.error("provide a report path or --latest")
    try: data=json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: cannot read report {path}: {exc}"); return 2
    errors=validate_report(data)
    if errors:
        for error in errors: print("FAIL:",error)
        print(f"RESULT: FAIL ({len(errors)} errors)")
        return 1
    print(f"RESULT: PASS — {data['report_id']} ({len(data['sources'])} sources, {len(data['claims'])} claims)")
    return 0

if __name__=="__main__": sys.exit(main())
