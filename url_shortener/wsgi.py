"""
WSGI config for url_shortener project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Load environment variables from .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortener.settings')

application = get_wsgi_application()
