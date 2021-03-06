"""
WSGI config for mobits_internet_banking project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mobits_internet_banking.settings")

application = get_wsgi_application()

# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:

import sys

path = '/home/viniciusalves/mobits_internet_banking'
if path not in sys.path:
    sys.path.append(path)