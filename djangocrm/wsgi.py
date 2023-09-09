"""
WSGI config for djangocrm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< Updated upstream
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
>>>>>>> Stashed changes
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrm.settings')

application = get_wsgi_application()
