#!/bin/bash

source classic_env
python3 manage.py makemigrations
python3 manage.py migrate
#python3 manage.py runserver 0:1337
gunicorn ba_website.wsgi:application --bind 127.0.0.1:1336