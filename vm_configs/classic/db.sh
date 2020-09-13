#!/bin/sh

apt install -y postgresql postgresql-client

systemctl enable postgresql@11-main
systemctl start postgresql@11-main