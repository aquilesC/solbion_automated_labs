import json

AUTHOR = 'Solbion'
SITENAME = 'Solbion'
SITEURL = ''

PATH = 'content'
THEME = 'themes/solbion'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Load landing page dynamic data
try:
    with open('.agents/landing_page.json', 'r') as f:
        data = json.load(f)
        LANDING_PAGE_SPEC = data.get('landing_page_specification', {})
        # Map sections by id for direct Jinja2 template access
        SECTIONS = {s['section_id']: s for s in LANDING_PAGE_SPEC.get('layout_structure', [])}
except Exception as e:
    print(f"Error loading landing_page.json: {e}")
    LANDING_PAGE_SPEC = {}
    SECTIONS = {}

# Load hardware page specification
try:
    with open('.agents/hardware.json', 'r') as f:
        data = json.load(f)
        HARDWARE_SPEC = data.get('hardware_page_specification', {})
        HARDWARE_SECTIONS = {s['section_id']: s for s in HARDWARE_SPEC.get('layout_structure', [])}
except Exception as e:
    print(f"Error loading hardware.json: {e}")
    HARDWARE_SPEC = {}
    HARDWARE_SECTIONS = {}

# Load services page specification
try:
    with open('.agents/services.json', 'r') as f:
        data = json.load(f)
        SERVICES_SPEC = data.get('services_page_specification', {})
        SERVICES_SECTIONS = {s['section_id']: s for s in SERVICES_SPEC.get('layout_structure', [])}
except Exception as e:
    print(f"Error loading services.json: {e}")
    SERVICES_SPEC = {}
    SERVICES_SECTIONS = {}

# Load data page specification
try:
    with open('.agents/data.json', 'r') as f:
        data = json.load(f)
        DATA_SPEC = data.get('data_page_specification', {})
        DATA_SECTIONS = {s['section_id']: s for s in DATA_SPEC.get('layout_structure', [])}
except Exception as e:
    print(f"Error loading data.json: {e}")
    DATA_SPEC = {}
    DATA_SECTIONS = {}

# Load contact page specification
try:
    with open('.agents/contact.json', 'r') as f:
        data = json.load(f)
        CONTACT_SPEC = data.get('contact_page_specification', {})
        CONTACT_SECTIONS = {s['section_id']: s for s in CONTACT_SPEC.get('layout_structure', [])}
except Exception as e:
    print(f"Error loading contact.json: {e}")
    CONTACT_SPEC = {}
    CONTACT_SECTIONS = {}

# Pelican paths configuration
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'extra']

# Extra path metadata to copy custom assets (e.g. CNAME, robots.txt, favicon)
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Feed generation (disabled for local development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social & Navigation are dynamically loaded from JSON (SECTIONS.global_navigation)

# Pagination
DEFAULT_PAGINATION = False

# Enable relative URLs for easier local previewing
RELATIVE_URLS = True

# Clean URLs for pages
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
