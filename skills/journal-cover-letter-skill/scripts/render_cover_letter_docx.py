#!/usr/bin/env python3
"""Render a validated structured payload as a privacy-scrubbed DOCX."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def build(payload: dict, output: Path) -> None:
    try:
        from docx import Document
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.shared import Inches, Pt
    except ImportError as exc:
        raise SystemExit("python-docx is required") from exc

    document = Document()
    section = document.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    style = document.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(8)
    style.paragraph_format.line_spacing = 1.08

    if payload.get("date"):
        document.add_paragraph(payload["date"])
    if payload.get("recipient_block"):
        for line in payload["recipient_block"]:
            document.add_paragraph(line)
    document.add_paragraph(payload["salutation"])
    for text in payload["paragraphs"]:
        paragraph = document.add_paragraph(text)
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    document.add_paragraph(payload["signoff"])
    document.add_paragraph(payload["corresponding_author"])
    if payload.get("affiliation"):
        document.add_paragraph(payload["affiliation"])
    if payload.get("contact"):
        document.add_paragraph(payload["contact"])

    props = document.core_properties
    props.author = ""
    props.last_modified_by = ""
    props.title = "Academic Journal Cover Letter"
    props.subject = ""
    props.comments = ""
    props.keywords = ""
    props.category = ""
    document.save(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("payload", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.payload.read_text(encoding="utf-8"))
    from validate_payload import validate

    errors = validate(payload)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2), file=sys.stderr)
        return 1
    build(payload, args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
