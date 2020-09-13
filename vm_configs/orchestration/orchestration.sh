#!/bin/sh

apt update
#apt upgrade -y
apt install -y htop glances tmux nload curl
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILJ2Y4h64RVSmA2p3p2kkvi5k/ixsFxXxqxPg2DjqHpw neil@ciri" >> /home/vagrant/.ssh/authorized_keys

curl -sfL https://get.k3s.io | sh -
#cp /vagrant/k3s/registries/registries.yml /etc/rancher/k3s/registries.yml