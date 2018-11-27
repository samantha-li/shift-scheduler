"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

=======
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
>>>>>>> 8bf5e16791af5989c93baf0971df91b517c89780
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
