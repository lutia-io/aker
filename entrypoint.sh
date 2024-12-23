#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD \
DJANGO_SUPERUSER_USERNAME=$SUPER_USER_NAME \
DJANGO_SUPERUSER_EMAIL=$SUPER_USER_EMAIL \
python manage.py createsuperuser --no-input

gunicorn aker.wsgi:application --bind :8000