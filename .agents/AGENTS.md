# Solbion Automated Labs Project Rules & Customizations

This file outlines the project guidelines, technology stack, visual design constraints, and developer conventions for the Solbion static website.

## Technical Choices
- **Static Site Generator:** Pelican (configured via `pelicanconf.py`).
- **Python Environment:** Managed via `uv` using Python 3.12 (inside `.venv` virtual environment).
- **Styling:** TailwindCSS via the Tailwind v4 CLI (`npm run build:css` or `npm run dev` handles compilation). No direct Vanilla CSS unless required for scoped overrides.
- **Core Strategy:** Data-centric, high-fidelity layouts using Tailwind utility classes, subtle animations, and semantic HTML structure.

## Visual Identity (from brand_brief.json)
- **Primary Background:** Carbon Black (`#12161A`) — represents laboratory/vacuum environments.
- **Primary Text:** Titanium White (`#FFFFFF`).
- **Accent Color:** Laser Cyan (`#00F0FF`) — represents active learning paths, plasma plumes, and interaction elements.
- **Baseline Color:** Steel Grey (`#333F4A`) — used for layout borders, secondary text, and inactive data points.
- **Typography:**
  - **Headers:** `'Space Grotesk', 'Inter', sans-serif` (geometric, sharp, uniform weight).
  - **Body and Code:** `'Roboto Mono', 'Fira Code', monospace` (data-heavy, machine-readable, precise numerical layouts).

## Brand & Tone of Voice
- **Tone:** Hyper-pragmatic, confident, technically authoritative, and direct.
- **Key Message:** Moving from slow human-driven trial-and-error to closed-loop Bayesian optimization and active learning loops.
- **Logo Concept:** "The Lattice Matrix" (Hexagonal grid system representing packing in crystalline structures, with active cyan paths and glow-effect nodes).
- **Imagery Policy:** Macro-photography of hardware (plasma plumes, flanges, silicon wafers) and high-fidelity data visualizations. *Never* use generic stock photos of scientists in lab coats holding colored liquids.
