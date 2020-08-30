#AUDIOS
mkdir /var/lib/asterisk/sounds/healthcheck
cp audios/fax/01.mp3 /var/lib/asterisk/sounds/healthcheck/
cp audios/fax/02.mp3 /var/lib/asterisk/sounds/healthcheck/

#asterisk 
cp extensions_custom.conf /etc/asterisk/extensions_custom.conf
asterisk -rx 'dialplan reload'