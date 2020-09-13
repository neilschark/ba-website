#!/bin/sh

apt update
#apt upgrade -y
apt install -y htop glances tmux nload curl git
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
apt update
apt install -y docker-ce docker-ce-cli containerd.io docker-compose
systemctl enable docker
systemctl start docker
usermod -aG docker vagrant
mkdir ~/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILJ2Y4h64RVSmA2p3p2kkvi5k/ixsFxXxqxPg2DjqHpw neil@ciri" >> /home/vagrant/.ssh/authorized_keys