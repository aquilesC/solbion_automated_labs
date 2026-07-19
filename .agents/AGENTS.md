# Solbion Automated Labs Project Rules & Customizations

This file outlines the project guidelines, technology stack, visual design constraints, and developer conventions for the Solbion static website.

## Technical Choices
- **Static Site Generator:** Pelican (configured via `pelicanconf.py`).
- **Python Environment:** Managed via `uv` using Python 3.12 (inside `.venv` virtual environment).
- **Styling:** TailwindCSS via the Tailwind v4 CLI. **CRITICAL:** The style must always be compiled (`npm run build:css`) before committing changes, because the compiled version of the style (`style.css`) is what needs to be loaded into the template. There is no style compilation step on the cloud provider! No direct Vanilla CSS unless required for scoped overrides.
- **Core Strategy:** Data-centric, high-fidelity layouts using Tailwind utility classes, subtle animations, and semantic HTML structure.

## Visual Identity (from brand_brief.json)
- **Primary Background:** Warm Clinical Light (`#FAFAFA`) — evokes a bright, well-lit modern laboratory.
- **Secondary Background:** Light Grey Slate (`#F3F4F6`).
- **Card Surface:** Pure White (`#FFFFFF`).
- **Primary Text:** Slate Heading (`#1A202C`).
- **Secondary Text:** Charcoal Body (`#4A5568`).
- **Accent Color:** Lab Teal (`#005E7A`) — represents active interaction pathways and primary actions.
- **Secondary Highlight:** Terracotta Amber (`#E28743`) — represents discovered nodes and status badges.
- **Baseline Border:** Soft Grey (`#E2E8F0`).
- **Typography:**
  - **Headers:** `'Inter', 'Helvetica Neue', sans-serif` (clean, geometric, spacious tracking).
  - **Body:** `'Inter', 'Segoe UI', sans-serif` (highly legible sans-serif font).
  - **Technical and Code:** `'JetBrains Mono', 'Fira Code', monospace` (precise data and code blocks).

## Brand & Tone of Voice
- **Archetype:** The Collaborative Evangelist.
- **Tone:** Transparent, Educational, Empowering, Authoritative yet approachable.
- **Communication Style:** Like a senior engineer sharing a breakthrough methodology with a peer. Focuses on multiplying capabilities and building ecosystems rather than enforcing vendor lock-in.
- **Logo Concept:** "The Lattice Matrix" (Hexagonal grid representing packing in crystalline structures, with soft grey background dots, Lab Teal paths, and Terracotta Amber nodes).
- **Imagery Policy:** Macro-photography of hardware (plasma plumes, flanges, silicon wafers) and high-fidelity data visualizations. *Never* use generic stock photos of scientists in lab coats holding colored liquids.
