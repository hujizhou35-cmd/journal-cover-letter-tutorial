# Output and DOCX

Deliver the letter text first, followed by a compact audit and unresolved items. Default to English; preserve scientifically important terminology when the user requests another language.

Use `assets/cover-letter-template.md` as a structure, not a rigid prose template. Apply length constraints in this order: explicit journal rule, explicit user request, submission-system limit, evidence-based journal convention, then the shortest length that completes the editorial function. Do not enforce a universal page or word limit.

For DOCX output, use `scripts/render_cover_letter_docx.py` with a validated JSON payload. Use a restrained business-letter layout, strip personal metadata, and confirm no unresolved placeholders. If a previous DOCX controls formatting and the user granted format permission, inherit only safe layout properties; never carry over hidden text, comments, tracked changes, document properties, old journal names, or old submission details.

Render the generated DOCX to page images and inspect every page before delivery. If rendering is unavailable, state that visual QA was not completed and still perform structural and metadata checks.
