#!/bin/bash

cd /boot/ahid/srv/cert/

sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout private.key -out certificate.crt

sudo cp private.key /etc/ssl/private/
sudo cp certificate.crt /etc/ssl/certs/

#sudo nano /etc/apache2/sites-available/000-default.conf

sudo a2enmod ssl
sudo apache2ctl configtest
sudo systemctl restart apache2.service

#https://peppe8o.com/self-signed-certificate-https-in-raspberry-pi-with-apache/


sudo a2enmod rewrite
systemctl restart apache2

