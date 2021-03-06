"""
WSGI config for vidly project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this Procfile, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidly.settings')

application = get_wsgi_application()
