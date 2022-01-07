"""
WSGI config for mycoffee_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
#الملف دا عبارة عن ارشدات عملها لغة البايثون عشان يتعمل من خلال هذه الارشدات حلقة وصل بين السريفر وبين الفريم ورك عشان من الاخر كدا تقدر تنتج تبيطقات ويب من خلال لغة البايثون
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycoffee_project.settings')

application = get_wsgi_application()
