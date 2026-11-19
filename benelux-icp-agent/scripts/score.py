#!/usr/bin/env python3
"""Merge research JSON files into a scored CSV using rubric.yaml.

Usage: python scripts/score.py
Reads output/research/*.json, validates points against the rubric weights,
computes total and tier, writes data/targets_scored.csv.
"""
import csv
import json
import sys
from pathlib import Path

import yaml  # pip install pyyaml

ROOT = Path(__file__).resolve().parent.parent
rubric = yaml.safe_load((ROOT / "rubric.yaml").read_text())
weights = {c["id"]: c["weight"] for c in rubric["criteria"]}
tiers = sorted(rubric["tiers"].items(), key=lambda kv: -kv[1])


def tier_for(total: int) -> str:
    for name, minimum in tiers:
        if total >= minimum:
            return name
    return "C"


rows = []
for path in sorted((ROOT / "output" / "research").glob("*.json")):
    d = json.loads(path.read_text())
    gates_ok = all(d.get("gates", {}).values())
    scores = d.get("scores", {})
    problems = []
    total = 0
    for cid, weight in weights.items():
        pts = scores.get(cid, {}).get("points", 0)
        if not 0 <= pts <= weight:
            problems.append(f"{cid}={pts} outside 0-{weight}")
            pts = max(0, min(pts, weight))
        total += pts
    row = {
        "company": d.get("company", path.stem),
        "url": d.get("url", ""),
        "sub_category": d.get("sub_category", ""),
        "gates_pass": gates_ok,
        "total": total if gates_ok else 0,
        "tier": tier_for(total) if gates_ok else "Dropped",
        "confidence": d.get("confidence", ""),
        "why_now": " | ".join(d.get("why_now", [])),
        "saas_angle": d.get("saas_angle", ""),
        "flags": "; ".join(d.get("flags", []) + problems),
        **{cid: scores.get(cid, {}).get("points", 0) for cid in weights},
    }
    rows.append(row)

if not rows:
    sys.exit("No research files found in output/research/")

rows.sort(key=lambda r: -r["total"])
out = ROOT / "data" / "targets_scored.csv"
with out.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(f"Wrote {len(rows)} companies to {out}")
