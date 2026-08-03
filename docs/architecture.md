# How the Skill works

The Skill handles the scientific and editorial decisions. Small scripts handle tasks that can be checked mechanically, such as reading and creating DOCX files, finding placeholders, validating structured data, and scanning release packages for privacy risks.

```mermaid
flowchart TD
    A["Read manuscript files"] --> B["Show facts and main selling points"]
    B --> C{"Author confirms?"}
    C -- "No" --> D["Wait for author"]
    C -- "Yes" --> E["Check current journal guidance"]
    E --> F{"Journal information available?"}
    F -- "No" --> G["Return a draft that still needs journal verification"]
    F -- "Yes" --> H{"Article type"}
    H -- "Original Research" --> I["Build one discovery story"]
    H -- "Review" --> J["Explain the new understanding from the synthesis"]
    H -- "Other or unclear" --> K["Ask the author how to proceed"]
    I --> L["Draft and check the letter"]
    J --> L
    K --> L
    L --> M{"Facts, claims, and statements complete?"}
    M -- "Yes" --> N["Return final text, optional DOCX, and a short check"]
    M -- "No" --> O["Return the safest draft and list what remains"]
```

The Skill never labels a letter as ready when facts conflict, required statements are missing, the article type is unresolved, or current journal guidance could not be checked.
