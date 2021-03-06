"""settings.py

"""

import os

DEBUG = True

APP_DIR = os.path.dirname(os.path.abspath(__file__))

WWW_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

FREEZER_DESTINATION = WWW_ROOT

FREEZER_BASE_URL = "http://localhost"

FREEZER_REMOVE_EXTRA_FILES = False

FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite"]

FLATPAGES_ROOT = os.path.join(APP_DIR, "pages")

FLATPAGES_EXTENSION = ".md"