"""
WSGI config for creativefailsproject.

It exposes the WSGI callable as a module-level variable named ``creativefails``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_creativefails

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creativefails.settings')

creativefails= get_wsgi_creativefails()
