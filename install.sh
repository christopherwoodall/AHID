#!/bin/bash

cd /opt
mkdir ahid
#chmod 777 ahid/
#chown pi:pi ahid/

##########

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get-full-upgrade

##########

#sudo apt-get install -y git apache2 php libapache2-mod-php
#sudo systemctl enable --now apache2

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
#apt-get install -y hostapd dnsmasq wireless-tools iw wvdial avahi-daemon avahi-discover avahi-utils libnss-mdns mdns-scan
#########
#https://mtlynch.io/key-mime-pi/
#https://gist.github.com/drmalex07/298ab26c06ecf401f66c
#https://gist.github.com/naholyr/4275302
#


#############################################
# ENABLE HTTPS
$PRIVATE_KEY="/boot/ahid/srv/cert/private.key"

if [[ ! -f "${PRIVATE_KEY}" ]]; then
    #https://peppe8o.com/self-signed-certificate-https-in-raspberry-pi-with-apache/
    cd /boot/ahid/srv/cert/

    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout private.key -out certificate.crt

    sudo cp private.key /etc/ssl/private/
    sudo cp certificate.crt /etc/ssl/certs/

    #sudo nano /etc/apache2/sites-available/000-default.conf

    sudo a2enmod ssl
    sudo apache2ctl configtest
    sudo systemctl restart apache2.service

    sudo a2enmod rewrite
    systemctl restart apache2
fi

#############################################
#python -c "import numpy;print(numpy.__version__);print(numpy.__file__)";
sudo apt-get install -y libatlas3-base libssl-dev cmake build-essential libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev  libilmbase-dev libopenexr-dev libgstreamer1.0-dev libatlas-base-dev libjasper-dev libqtgui4 python3-pyqt5 libqt4-test

pip3 install opencv-contrib-python==3.4.2.17

#############################################
# Increase Swap
#https://raspberrypi.stackexchange.com/questions/70/how-to-set-up-swap-space
nano /etc/dphys-swapfile
#CONF_SWAPSIZE=1024
dphys-swapfile setup
sudo dphys-swapfile swapon
/etc/init.d/dphys-swapfile restart

#############################################
