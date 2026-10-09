"""
WSGI config for the project.

Elastic Beanstalk starts the app with gunicorn using the WSGIPath set in
.ebextensions/django.config:  mysite.wsgi:application
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")  # <-- change "mysite"

application = get_wsgi_application()
