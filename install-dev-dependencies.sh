#!/bin/bash

echo -e "\nInstalling dev dependencies..."
apt-get -y update
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo apt-get -y install curl
curl -sL https://deb.nodesource.com/setup_7.x | sudo -S -E bash -
sudo apt-get -y install nodejs
npm install -g newman
