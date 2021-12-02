#!/bin/bash


sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install -y git

apt-get install -y hostapd dnsmasq wireless-tools iw wvdial avahi-daemon avahi-discover avahi-utils libnss-mdns mdns-scan

sudo apt install -y apache2 php libapache2-mod-php
sudo systemctl enable --now apache2

# Create app directory
mkdir /opt/ahid
cd /opt/ahid
chmod +x /opt/ahid/hid.sh
#ln -s /opt/ahid/www /var/www/html


sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config


# Add USB Gadget Modules
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

# Create USB Gadget on Startup
sed -i 's/exit 0//g' /etc/rc.local
echo "/opt/ahid/hid.sh" >> /etc/rc.local
#echo "chmod 777 /dev/{hidg0,hidg1}" >> /etc/rc.local
echo "exit 0" >> /etc/rc.local


# symlink for hostapd?
#ln -s /boot/ahid/hostapd.conf /etc/hostapd/hostapd.conf

#########
#https://mtlynch.io/key-mime-pi/
#https://gist.github.com/drmalex07/298ab26c06ecf401f66c
#https://gist.github.com/naholyr/4275302
#
