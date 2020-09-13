#!/bin/bash

yarn install
yarn run build
sudo mkdir -p /app
sudo cp ../nginx/classic/nginx.conf /etc/nginx/nginx.conf
sudo cp -r ./dist/. /app
sudo nginx