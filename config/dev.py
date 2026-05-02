"""
Development settings for The Creator's Bulwark.
"""

import os
from .base import *  # noqa: F401, F403
from .database import build_database_config, disable_server_side_cursors

DEBUG = os.getenv("DEBUG", "false" if os.getenv("VERCEL") else "true").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}

# Use Supabase/Postgres DATABASE_URL when present; otherwise fallback to SQLite.
DATABASES = build_database_config(BASE_DIR)
DISABLE_SERVER_SIDE_CURSORS = disable_server_side_cursors()

# CORS - allow all only in local development.
CORS_ALLOW_ALL_ORIGINS = DEBUG

# Email backend - console for dev
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
