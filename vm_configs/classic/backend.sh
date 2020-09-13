#!/bin/sh

apt install -y nginx python3-pip gunicorn python3-venv
pip3 install --global poetry
sudo adduser --system --no-create-home --shell /bin/false --group --disabled-login nginx