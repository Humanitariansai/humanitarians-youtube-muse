#!/usr/bin/env python3
"""Apply Canvas-safe inline styles to the pandoc-generated pages in this folder.

Canvas's rich-content editor strips <style> blocks and unknown classes, so table
borders and blockquote rules have to be inline. Run after regenerating with pandoc:

    cd frictional && for f in 0*.md; do
        pandoc "$f" -f gfm -t html5 --wrap=preserve -o "html/${f%.md}.html"
    done && python3 html/_style.py
"""
import pathlib
import re

TABLE = 'style="border-collapse:collapse;width:100%;margin:1em 0;"'
TH = ('style="border:1px solid #c7c7c7;padding:8px 10px;text-align:left;'
      'background:#f2f2f2;vertical-align:top;"')
TD = 'style="border:1px solid #c7c7c7;padding:8px 10px;vertical-align:top;"'
BQ = 'style="border-left:4px solid #8a8a8a;margin:1em 0;padding:0.6em 1em;background:#f7f7f7;"'
HR = 'style="border:0;border-top:1px solid #d9d9d9;margin:2em 0;"'
PRE = ('style="background:#f2f2f2;border:1px solid #d9d9d9;padding:10px 12px;'
       'overflow-x:auto;white-space:pre;"')

REPO = "https://github.com/nikbearbrown/info-7375-branding-and-ai-fall-2026/blob/main"


def absolutize(html):
    """Rewrite repo-relative .md links to GitHub URLs.

    Canvas pages are served from a different origin, so a relative link to
    ../prerequisites/frictional.md resolves to nothing. Students in this course
    already read the repo, so point every link there.
    """
    html = re.sub(r'href="\.\./([^"]+\.md)"', rf'href="{REPO}/\1"', html)
    html = re.sub(r'href="(0\d-[^"/]+\.md)"', rf'href="{REPO}/frictional/\1"', html)
    html = re.sub(r'href="(templates/[^"]+\.md)"',
                  rf'href="{REPO}/frictional/\1"', html)
    return html

for path in sorted(pathlib.Path(__file__).parent.glob("*.html")):
    s = path.read_text()
    s = s.replace("<table>", f"<table {TABLE}>")
    s = re.sub(r"<th([ >])", lambda m: f"<th {TH}{m.group(1)}", s)
    s = re.sub(r"<td([ >])", lambda m: f"<td {TD}{m.group(1)}", s)
    s = s.replace("<blockquote>", f"<blockquote {BQ}>")
    s = s.replace("<hr />", f"<hr {HR} />")
    s = s.replace("<pre>", f"<pre {PRE}>")
    # pandoc adds its own text-align on aligned cells; drop the duplicate attribute
    s = re.sub(r'(<t[hd] style="[^"]*")\s+style="text-align:\s*\w+;"', r"\1", s)
    s = absolutize(s)
    path.write_text(s)
    print(f"styled {path.name}")
