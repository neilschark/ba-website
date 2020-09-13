#!/bin/sh

apt install -y postgresql postgresql-client
systemctl enable postgresql@11-main
systemctl start postgresql@11-main

#mv /vagrant/vm_configs/classic/postgresql.conf /etc/postgresql/11/main/postgresql.conf
mv /vagrant/vm_configs/classic/postgresql2.conf /etc/postgresql/11/main/postgresql.conf
chown postgres:postgres /etc/postgresql/11/main/postgresql.conf

apt install -y python3-pip python3-venv
pip3 install --global poetry
apt install -y nginx
sudo adduser --system --no-create-home --shell /bin/false --group --disabled-login nginx

curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh
bash nodesource_setup.sh
apt install -y nodejs
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
apt update && apt install -y yarn
