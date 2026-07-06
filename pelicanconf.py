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
        LANDING_PAGE = json.load(f).get('landing_page', {})
except Exception as e:
    print(f"Error loading landing_page.json: {e}")
    LANDING_PAGE = {}

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

# Social & Navigation (Can be customized or expanded in templates)
NAV_ITEMS = [
    ('Technology', '#technology'),
    ('Applications', '#applications'),
    ('Data Factory', '#data-factory'),
    ('Company', '#company'),
]

# Pagination
DEFAULT_PAGINATION = False

# Enable relative URLs for easier local previewing
RELATIVE_URLS = True
