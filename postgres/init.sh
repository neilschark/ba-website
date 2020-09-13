#!/bin/sh

sudo -u postgres createuser -s -i -d -r -l -w root
sudo -u postgres psql -c "ALTER ROLE root WITH PASSWORD '1234';"
sudo -u postgres createuser -s -i -d -r -l -w vagrant
sudo -u postgres psql -c "ALTER ROLE vagrant WITH PASSWORD '1234';"
createdb ba-db