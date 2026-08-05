# Output and DOCX v3.0

Deliver the letter text first, followed by a compact audit and unresolved items. The audit must include exact official article type, intellectual route, empirical anchor, editorial meaning, route-specific spine or thesis, journal-fit evidence, and metric boundary when applicable.

Use `assets/cover-letter-template.md` as a structure, not a rigid prose template. Do not enforce a universal page or word limit.

For DOCX output, use `scripts/render_cover_letter_docx.py` with a validated JSON payload. Use a restrained business-letter layout, strip personal metadata, and confirm no unresolved placeholders. If a previous DOCX controls formatting and the user granted format permission, inherit only safe layout properties.

Render the generated DOCX to page images and inspect every page before delivery. If rendering is unavailable, state that visual QA was not completed and still perform structural and metadata checks.
