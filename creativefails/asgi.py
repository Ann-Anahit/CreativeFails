"""
ASGI config for creativefails project.

It exposes the ASGI callable as a module-level variable named ``creativefails``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_creativefails

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creativefails.settings')

creativefails = get_asgi_creativefails()
