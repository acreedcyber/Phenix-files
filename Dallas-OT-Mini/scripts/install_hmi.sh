#!/bin/bash
apt update
apt install -y nmap curl unzip
curl -LO https://www.modbusdriver.com/downloads/modpoll.zip
unzip modpoll.zip
chmod +x modpoll
mv modpoll /usr/local/bin/
