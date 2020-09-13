#!/bin/sh

sleep 5
python3 manage.py makemigrations
python3 manage.py migrate
#python3 manage.py runserver 0:1337
gunicorn ba_website.wsgi:application --bind 0.0.0.0:1337