---
description: Unified workflow for Google Stitch CLI — manage projects, generate AI screens, inspect design systems, and capture frontend code to Canvas.
---

# Workflow: `/stitch`

Manage Google Stitch CLI operations directly from Antigravity.

## Core Operations

### 1. Status & Auth
```bash
stitch status --json
```

### 2. Project Management
```bash
# List recent projects
stitch find projects --limit 5 --json

# Create new Stitch canvas project
stitch create project --title "<Project Name>" --json

# Bind default project
stitch config set project <PROJECT_ID>
```

### 3. Screen Generation
```bash
stitch generate screen \
  --project <PROJECT_ID> \
  --device MOBILE \
  --title "<Screen Title>" \
  --prompt "<Art-directed UI prompt>" \
  --json
```

### 4. Screen Variations
```bash
stitch generate variant \
  --project <PROJECT_ID> \
  --screen <SCREEN_ID> \
  --count 3 \
  --creative-range REFINE \
  --prompt "Refine card elevations and optimize contrast" \
  --json
```

### 5. Capture & Dev Server
```bash
# Capture local web route into self-contained HTML
stitch capture http://localhost:8080/ -o .stitch/captured.html --json

# Upload captured screen
stitch upload screen .stitch/captured.html --route / --title "Production App" --json

# Open Canvas in browser
stitch open project <PROJECT_ID>
```
