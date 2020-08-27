
#installations
sudo apt-get install sendemail git python python-pip

sudo apt autoremove

pip3 install gpiozero

#AUDIOS
mkdir /var/lib/asterisk/sounds/healthcheck
cp audios/fax/01.mp3 /var/lib/asterisk/sounds/healthcheck/
cp audios/fax/02.mp3 /var/lib/asterisk/sounds/healthcheck/

#asterisk 
cp extensions_custom.conf /etc/asterisk/extensions_custom.conf
asterisk -rx 'dialplan reload'