#!/usr/bin/env python3
"""Validate the NEU teaching layer without inspecting historical student records."""
import json
import re
from pathlib import Path
from urllib.parse import unquote
ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "course-layer-manifest.json").read_text())
course = json.loads((ROOT / "course.json").read_text())
errors = []
stages = ["Predict", "Build It", "Use It", "Ship It", "Verify"]
policy = "https://youtu.be/8Ut0Cdl6vMw?si=9w3aEpt1ZyAR4Kiz"
def check(condition, message):
    if not condition:
        errors.append(message)
check(course["pedagogy"] == stages, "Wrong pedagogy")
check(course["points"] == {"implementation": 60, "frictional": 10, "github": 10, "relative_quartile": 20}, "Wrong point allocation")
check(len(course["lessons"]) == 15, "Expected 15 lessons")
check(len(course["assignments"]) == 10, "Expected 10 assignments")
covered = []
read_chapters = set()
for lesson in course["lessons"]:
    for reading in lesson["readings"]:
        check((ROOT / reading).is_file(), "Missing grouped reading: " + reading)
        read_chapters.add(int(Path(reading).name[:2]))
    check((ROOT / lesson["reading"]).is_file(), "Missing reading: " + lesson["reading"])
    text = (ROOT / lesson["path"]).read_text()
    headings = re.findall(r"^## (Predict|Build It|Use It|Ship It|Verify)$", text, re.M)
    check(headings == stages, "Wrong stage order: " + lesson["path"])
    check("Assessments — ungraded" in text, "Missing ungraded label: " + lesson["path"])
    if "## Irreducibly Human" in text:
        check("**AI should**" in text and "**Human should**" in text, "Missing division of labor")
for assignment in course["assignments"]:
    covered.extend(assignment["lessons"])
    text = (ROOT / assignment["path"]).read_text()
    check(policy in text, "Missing policy: " + assignment["path"])
    check("**AI should**" in text and "**Human should**" in text, "Missing assignment division of labor")
    check(re.findall(r"^## (Predict|Build It|Use It|Ship It|Verify)$", text, re.M) == stages, "Wrong assignment stage order")
    table = text.split("## Rubric — 100 points", 1)[1]
    values = [int(v) for v in re.findall(r"^\|[^|]+\|\s*\**(\d+)\**\s*\|", table, re.M)]
    check(values == [8, 22, 12, 12, 6, 60, 10, 10, 20, 100], "Rubric mismatch: " + assignment["path"])
    check(sum(values[:5]) == 60 and sum(values[6:9]) == 40, "Rubric sum incorrect")
check(sorted(covered) == list(range(1, 16)), "Assignments must cover each lesson exactly once")
check(read_chapters == set(range(1, 20)), "Must cover all 19 core chapters")
companion_links = 0
for name in manifest["files"]:
    p = ROOT / name
    check(p.is_file(), "Missing course-layer file: " + name)
    if p.suffix != ".md" or not p.exists():
        continue
    text = p.read_text()
    check(not re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.M), "Conflict marker in course layer: " + name)
    check("fall-2025/" not in text, "Stale submission term: " + name)
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0].strip("<>")
        if not target or re.match(r"[a-z]+:", target):
            continue
        resolved = (p.parent / unquote(target)).resolve()
        if not resolved.is_relative_to(ROOT):
            companion_links += 1
            check(resolved.exists(), "Missing local companion link: " + name + " -> " + target)
        else:
            check(resolved.exists(), "Broken link: " + name + " -> " + target)
if errors:
    for error in errors:
        print("FAIL:", error)
    raise SystemExit(1)
print("PASS: 15 five-stage lessons; 10 assignments covering all lessons; 100-point rubrics; policy links; local reading and document links.")
print(f"Checked {len(manifest['files'])} course-layer files and {companion_links} optional local companion links.")
print("This check does not execute student implementations, verify external URLs, or certify manuscript factual accuracy.")
