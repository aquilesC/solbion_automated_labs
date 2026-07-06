# Solbion Automated Labs

> **The autonomous engine for materials discovery. A data factory for the physical world.**

Solbion is a high-performance, automated platform designed to accelerate materials discovery by transitioning from slow, sequential human-driven trial-and-error to closed-loop Bayesian optimization and active learning loops. This repository hosts the static landing page and platform dashboard architecture for Solbion.

---

## 🌌 Brand Identity & Visual Guidelines

Solbion's aesthetic reflects high-vacuum chamber physics, automated metrology, and high-throughput physical experimentation:

- **Carbon Black (`#12161A`)**: Primary background representing clean laboratory/vacuum chamber environments.
- **Titanium White (`#FFFFFF`)**: High-contrast typography for primary copy and headings.
- **Laser Cyan (`#00F0FF`)**: Dynamic accent representing active learning paths, plasma plumes, and interactive widgets.
- **Steel Grey (`#333F4A`)**: Baseline borders, secondary data points, and lattice grid elements.
- **The Lattice Matrix**: The core brand logo geometry represents close-packed crystalline lattices with glowing active nodes charting discovered, optimized multi-dimensional spaces.

---

## 🛠️ Technology Stack

The project relies on a hybrid static generation and assets orchestration workflow:

- **Static Site Generator**: [Pelican](https://getpelican.com/) (configured via `pelicanconf.py`)
- **Styling**: [TailwindCSS v4.0](https://tailwindcss.com/) managed via `@tailwindcss/cli`
- **Environment Management**: Python 3.12+ (dependencies managed via `requirements.txt`)
- **Node.js Orchestration**: `npm` for building/watching styles concurrently with the Pelican dev server.

---

## 📂 Project Structure

```bash
solbion_automated_labs/
├── .agents/                 # Workspace customizations, AGENTS.md, brand briefs, & landing datasets
│   ├── AGENTS.md            # Agent instructions and workspace rules
│   ├── brand_brief.json     # Curated brand tokens, colors, taglines, and vocabulary
│   └── landing_page.json    # Structurally unified content feed for the landing page
├── content/                 # Site content (markdown pages and articles)
├── themes/
│   └── solbion/             # Custom theme templates and static stylesheets
│       ├── static/          # Custom CSS (compiled tailwind output)
│       └── templates/       # Jinja2 template files (index, base, page, tags, etc.)
├── pelicanconf.py           # Core configuration for Pelican
├── publishconf.py           # Production release configurations for Pelican
├── package.json             # npm dependencies, tailwind build scripts, development server scripts
├── requirements.txt         # Python package dependencies
└── README.md                # Project documentation (this file)
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.12+**
- **Node.js 18+** & **npm**

### 1. Set Up Python Environment
Create and activate a virtual environment, then install Python dependencies:
```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 2. Set Up Node & npm Dependencies
Install the package manager dependencies (includes TailwindCSS v4 and concurrently):
```bash
npm install
```

### 3. Run the Development Server
Start the concurrent development environment to automatically compile Tailwind CSS changes and reload Pelican on port `8123`:
```bash
npm run dev
```
Open [http://localhost:8123](http://localhost:8123) in your browser.

### 4. Build for Production
Generate the optimized static output inside the `output/` directory:
```bash
npm run build
```

---

## ☁️ Deployment on Cloudflare Pages

To deploy this project on Cloudflare Pages, configure the application with the following build settings in the Cloudflare Dashboard:

1. **Framework Preset**: `None`
2. **Build Command**: `pip install -r requirements.txt && npm run build`
3. **Build Directory / Output Directory**: `output`
4. **Environment Variables**:
   - `PYTHON_VERSION`: `3.12` (or the version matching your python runtime)
   - `NODE_VERSION`: `18` (or greater, if required by npm packages)

---

## 📝 Contribution & Code Style

- **Keep It Semantic**: Ensure all templates and pages use valid HTML5 semantic tags.
- **Maintain Style Sync**: Write styles in `themes/solbion/static/css/src/style.css` and let Tailwind CLI build into the active output directory.
- **Follow the Agent Rules**: Read and respect instructions inside `.agents/AGENTS.md` before making design iterations.
