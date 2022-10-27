#!/usr/bin/env python
"""
Command-line utility for administrative tasks.

# For more information about this file, visit
# https://docs.djangoproject.com/en/2.1/ref/django-admin/
"""

import os
import sys
from dotenv import load_dotenv

def main():
    load_dotenv()

    settings_module = "web.settings.production" if 'WEBSITE_HOSTNAME' in os.environ else "web.settings.development"
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        settings_module)

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