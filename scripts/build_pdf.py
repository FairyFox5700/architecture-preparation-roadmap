from __future__ import annotations

import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

import markdown
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ARCHITECTURE_PREPARATION_ROADMAP.md"
HTML = ROOT / "print.html"
TMP_PDF = ROOT / "architecture-roadmap.tmp.pdf"
OUTPUT = ROOT / "ARCHITECTURE_PREPARATION_ROADMAP.pdf"
CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

CSS = r"""
@page {
  size: A4;
  margin: 17mm 17mm 19mm 17mm;
  @bottom-center {
    content: "Iryna Tyshchenko  •  Architecture Preparation  •  " counter(page);
    color: #667085;
    font-size: 8.5pt;
  }
}
* { box-sizing: border-box; }
html { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
body {
  margin: 0;
  color: #17223b;
  background: white;
  font: 10.2pt/1.5 "Segoe UI", Arial, sans-serif;
}
a { color: #1658a6; text-decoration: none; overflow-wrap: anywhere; }
.cover {
  page-break-after: always;
  height: 250mm;
  padding: 25mm 17mm 18mm;
  color: white;
  background:
    radial-gradient(circle at 85% 12%, rgba(232,122,45,.75), transparent 25%),
    linear-gradient(145deg, #101d4f 0%, #1b2a6b 56%, #29499a 100%);
  position: relative;
  overflow: hidden;
}
.cover:after {
  content: "";
  position: absolute;
  width: 155mm; height: 155mm;
  right: -65mm; bottom: -72mm;
  border: 2px solid rgba(255,255,255,.18);
  border-radius: 50%;
  box-shadow: 0 0 0 18mm rgba(255,255,255,.035), 0 0 0 38mm rgba(255,255,255,.025);
}
.kicker {
  display: inline-block;
  padding: 7px 12px;
  border-radius: 999px;
  background: #f6c8aa;
  color: #1b2a6b;
  font-size: 9pt;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.cover h1 { font-size: 31pt; line-height: 1.08; margin: 24mm 0 7mm; max-width: 145mm; color: white; }
.cover h2 { font-size: 15pt; line-height: 1.35; font-weight: 500; color: #e5ebff; max-width: 150mm; border: 0; }
.cover .meta { margin-top: 28mm; font-size: 11pt; line-height: 1.75; color: #edf1ff; }
.cover .author { position: absolute; bottom: 23mm; left: 17mm; font-weight: 650; color: white; }
.toc-page { page-break-after: always; }
.toc-page h1 { margin-top: 0; }
.toc { column-count: 2; column-gap: 9mm; }
.toc ul { list-style: none; padding-left: 0; margin: 0; }
.toc > ul > li { margin-bottom: 2mm; }
.toc li { break-inside: avoid; margin: 0 0 4px; font-size: 9.4pt; }
.toc li li { padding-left: 10px; font-size: 8.9pt; }
.toc a { color: #1b2a6b; }
h1 {
  color: #1b2a6b;
  font-size: 22pt;
  line-height: 1.2;
  margin: 0 0 9mm;
  page-break-before: auto;
  break-before: auto;
  border-bottom: 4px solid #e87a2d;
  padding-bottom: 4mm;
}
h2 {
  color: #1b2a6b;
  font-size: 15pt;
  line-height: 1.25;
  margin: 9mm 0 4mm;
  border-bottom: 1px solid #cad3eb;
  padding-bottom: 2mm;
  break-after: avoid;
}
h3 {
  color: #29499a;
  font-size: 11.7pt;
  margin: 6mm 0 2mm;
  break-after: avoid;
}
p { margin: 0 0 3.2mm; orphans: 3; widows: 3; }
ul, ol { margin: 1.5mm 0 4mm 5mm; padding-left: 5mm; }
li { margin: 0 0 1.6mm; }
li > ul, li > ol { margin-top: 1.3mm; }
blockquote {
  margin: 5mm 0;
  border-left: 4px solid #e87a2d;
  background: #fff4ec;
  padding: 4mm 5mm;
  color: #493528;
}
code { background: #eef2fb; color: #1b2a6b; border-radius: 3px; padding: 1px 3px; }
pre {
  white-space: pre-wrap;
  background: #101d4f;
  color: #f7f9ff;
  padding: 4mm;
  border-radius: 6px;
  font-size: 8.7pt;
  break-inside: avoid;
}
hr { border: 0; border-top: 1px solid #d6dceb; margin: 8mm 0; }
strong { color: #12245f; }
.citation-note {
  background: #eef6f1;
  border: 1px solid #b8d8c5;
  color: #214d35;
  padding: 3mm 4mm;
  border-radius: 5px;
  margin-bottom: 7mm;
}
#sources + ul, #sources ~ ul { font-size: 9pt; line-height: 1.4; margin-bottom: 2.5mm; }
#sources ~ ul li { break-inside: avoid; margin-bottom: 1.8mm; }
#the-shortest-effective-path { break-before: page; page-break-before: always; }
@media print {
  h1, h2, h3 { page-break-after: avoid; }
  li, blockquote, pre { page-break-inside: avoid; }
}
"""


def normal(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def source_link(match: re.Match[str]) -> str:
    number, url = match.group(1), match.group(2)
    parsed = urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    suffix = " / ".join(parts[-2:]) if parts else "home"
    label = f"{parsed.netloc} — {suffix}"
    return f"- **[{number}]** [{label}]({url})"


def prepare_markdown(source: str) -> tuple[str, list[tuple[int, str]]]:
    # The cover duplicates the title metadata; start print body after the first rule.
    parts = source.split("\n---\n", 1)
    body = parts[1] if len(parts) == 2 else source
    # Replace raw citation URLs with compact, clickable labels in print only.
    body = re.sub(r"(?m)^\[(\d+)\] (https?://\S+)$", source_link, body)
    body = body.replace("- [ ] ", "- ☐ ")
    headings = []
    for level, title in re.findall(r"(?m)^(#{1,2})\s+(.+?)\s*$", body):
        clean = re.sub(r"[*_`]", "", title)
        headings.append((len(level), clean))
    return body, headings


def build_html() -> list[tuple[int, str]]:
    source = SOURCE.read_text(encoding="utf-8")
    body_md, headings = prepare_markdown(source)
    md = markdown.Markdown(extensions=["toc", "tables", "fenced_code", "sane_lists"], extension_configs={"toc": {"permalink": False, "toc_depth": "1-2"}})
    body_html = md.convert(body_md)
    toc_html = md.toc
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Architecture Preparation Roadmap — Iryna Tyshchenko</title>
<style>{CSS}</style></head><body>
<section class="cover">
  <span class="kicker">Targeted 12-week roadmap</span>
  <h1>Architecture Preparation Roadmap</h1>
  <h2>Azure · Distributed Systems · Agentic AI · FDE Readiness</h2>
  <div class="meta">
    Project-led curriculum<br>
    Current certification strategy<br>
    Curated primary-source library<br>
    Production-readiness scorecards
  </div>
  <div class="author">Iryna Tyshchenko · October 2026</div>
</section>
<section class="toc-page">
  <h1>Contents</h1>
  <p class="citation-note">Use the roadmap sequentially. Use the resource library selectively. Certifications validate demonstrated ability; they do not replace architecture evidence.</p>
  <div class="toc">{toc_html}</div>
</section>
<main>{body_html}</main>
</body></html>"""
    HTML.write_text(html, encoding="utf-8")
    return headings


def print_pdf() -> None:
    if not CHROME.exists():
        raise FileNotFoundError(CHROME)
    uri = HTML.resolve().as_uri()
    subprocess.run([
        str(CHROME), "--headless=new", "--disable-gpu", "--no-sandbox",
        "--disable-extensions", "--no-pdf-header-footer",
        f"--print-to-pdf={TMP_PDF}", uri,
    ], check=True, timeout=180)


def add_metadata_and_bookmarks(headings: list[tuple[int, str]]) -> None:
    reader = PdfReader(str(TMP_PDF))
    page_text = [normal(page.extract_text() or "") for page in reader.pages]
    writer = PdfWriter(clone_from=str(TMP_PDF))
    writer.add_metadata({
        "/Title": "Architecture Preparation Roadmap",
        "/Author": "Iryna Tyshchenko",
        "/Subject": "Azure, distributed systems, agentic AI, FDE readiness, and certification strategy",
        "/Keywords": "Azure, architecture, distributed systems, agentic AI, FDE, AZ-305, AI-103, AB-100",
    })
    parent = None
    used = set()
    for level, title in headings:
        needle = normal(title)
        page_no = next((i for i, text in enumerate(page_text) if needle in text), None)
        if page_no is None or (level, title, page_no) in used:
            continue
        used.add((level, title, page_no))
        if level == 1:
            parent = writer.add_outline_item(title, page_no)
        elif parent is not None:
            writer.add_outline_item(title, page_no, parent=parent)
    with OUTPUT.open("wb") as fh:
        writer.write(fh)


def verify() -> None:
    reader = PdfReader(str(OUTPUT))
    if len(reader.pages) < 10:
        raise RuntimeError(f"Unexpectedly short PDF: {len(reader.pages)} pages")
    text = normal("\n".join(page.extract_text() or "" for page in reader.pages))
    expected = [
        "Twelve-week project-led roadmap",
        "Certification strategy for current architect roles",
        "Targeted resource library",
        "Architecture review scorecard",
        "Final production-readiness checklist",
        "Sources",
    ]
    missing = [x for x in expected if x.lower() not in text.lower()]
    if missing:
        raise RuntimeError(f"Missing expected text: {missing}")
    external_links = 0
    for page in reader.pages:
        for ref in page.get("/Annots", []):
            obj = ref.get_object()
            action = obj.get("/A")
            if action and action.get("/URI"):
                external_links += 1
    if external_links < 20:
        raise RuntimeError(f"Too few external hyperlinks: {external_links}")
    if not reader.outline:
        raise RuntimeError("PDF has no bookmarks")
    print({"pdf": str(OUTPUT), "pages": len(reader.pages), "external_links": external_links, "bookmarks": len(reader.outline)})


if __name__ == "__main__":
    headings = build_html()
    print_pdf()
    add_metadata_and_bookmarks(headings)
    verify()
    TMP_PDF.unlink(missing_ok=True)
