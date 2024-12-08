#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

def main():
    """Run administrative tasks."""
    # Load environment variables from .env
    BASE_DIR = Path(__file__).resolve().parent.parent
    load_dotenv(dotenv_path=BASE_DIR / '.env')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortener.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
