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
