# Benelux Hardware ICP: Research and Scoring Agent

## Goal
Find and rank Benelux hardware companies that fit the Mendix ISV ICP, so Kevin only reviews the top tier before outreach.

## ICP (short)
Hardware makers in regulated or critical industries whose core business is not software. Changing regulation or market pressure forces them to innovate. Mendix (governance, security, compliance) lets them build a SaaS around their product and data.

- Wave 1: Test & Measurement (metrology and adjacent measuring instruments), Medical Devices, Industrial Machinery
- Wave 2: Food & Beverage, Boats & Submarines, Electronics, Photographic & Optical
- Overlap: Industrial Machinery overlaps with Marco's campaign. Flag overlaps, do not drop silently.

## Project layout
- `rubric.yaml` : gates, weighted criteria, tiers (single source of truth)
- `prompts/research_agent.md` : prompt used to research one company
- `data/targets.csv` : input list (ZoomInfo export) plus scored results
- `scripts/score.py` : validates criterion points against the rubric, computes total and tier
- `output/` : generated reports and later the dashboard

## Workflow
1. Put companies in `data/targets.csv` (name, website, sub_category, employees, city).
2. For each company, research it using `prompts/research_agent.md` and the web, then write the result as JSON in `output/research/<slug>.json`.
3. Run `python scripts/score.py` to merge results into `data/targets_scored.csv`.
4. Review Tier A only. Never send outreach automatically.

## Rules
- Use only facts from sources actually opened. No evidence means 0 points and "no evidence found".
- Every score needs a one-line evidence note and a source URL.
- Keep quotes from sources to a few words.
- Calibrate first: 10-15 companies Kevin scored by hand, compare, tune `rubric.yaml`.

## Next steps
- Calibration run on known companies
- Dashboard in `output/` (tier funnel, score distribution, sub-category breakdown, top companies table)
- Monthly trigger refresh for Tier B and C
