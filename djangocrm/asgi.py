"""
ASGI config for djangocrm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< Updated upstream
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
>>>>>>> Stashed changes
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrm.settings')

application = get_asgi_application()
