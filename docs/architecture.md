# Architecture

## Design boundary

The Skill instructions perform semantic work: manuscript interpretation, contribution ranking, Research story selection, Review field diagnosis, editorial-thesis selection, journal-conversation synthesis, and claim calibration.

Deterministic scripts perform operations that can be checked mechanically: DOCX extraction and rendering, structured payload validation, placeholder detection, risk-term flagging, audit serialization, package construction, and privacy scanning.

This separation avoids pretending that keyword rules can judge scientific novelty or editorial value.

## State flow

```mermaid
flowchart TD
    A["Input files"] --> B["Fact Sheet: verified / conflict / missing"]
    B --> C{"Author confirms facts and route?"}
    C -- No --> D["NEEDS_AUTHOR_CONFIRMATION"]
    C -- Yes --> E["Current official journal research"]
    E --> F{"Official information available?"}
    F -- No --> G["NEEDS_JOURNAL_VERIFICATION"]
    F -- Yes --> H{"Article type"}
    H -- Original Research --> I["Select scientific story angle"]
    H -- Review / Synthesis --> J["Field diagnosis + synthesis intervention + editorial thesis"]
    H -- Other --> K["Confirm fallback"]
    I --> L["Controlled uplift + draft loop"]
    J --> L
    K --> L
    L --> M["Hard and quality gates"]
    M -- Pass --> N["Adaptive length + DOCX / audit"]
    M -- Author input --> D
    M -- Unresolved at limit --> O["BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS"]
    N --> P["SUBMISSION_READY"]
```

## Final state rule

`SUBMISSION_READY` is impossible when current official journal information was unavailable, a fact conflict remains, required declarations are incomplete, article type is unresolved, or prior-letter use exceeded permission.
