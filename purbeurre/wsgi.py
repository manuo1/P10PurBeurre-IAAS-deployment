"""WSGI config for purbeurre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import find_dotenv, load_dotenv
from django.core.wsgi import get_wsgi_application


"""this part will designate the right settings file """
"""to use depending on the environment"""
load_dotenv(find_dotenv())
environment = os.environ['ENVIRONMENT']
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
    'purbeurre.settings.{}'.format(environment))
""" end of environment settings part"""

application = get_wsgi_application()
