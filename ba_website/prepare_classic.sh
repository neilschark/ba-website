#!/bin/bash

sudo pip3 install poetry
#poetry config virtualenvs.create false && 
poetry install --no-dev
poetry shell