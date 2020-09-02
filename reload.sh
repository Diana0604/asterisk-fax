#AUDIOS
#mkdir /var/lib/asterisk/sounds/healthcheck
#cp audios/fax/01.mp3 /var/lib/asterisk/sounds/healthcheck/
#cp audios/fax/02.mp3 /var/lib/asterisk/sounds/healthcheck/

#asterisk 
cp extensions_custom.conf /etc/asterisk/extensions_custom.conf
asterisk -rx 'dialplan reload'

#mkdir /var/lib/asterisk/sounds/en/faxmachine
#cp audios/fax/01.wav /var/lib/asterisk/sounds/en/faxmachine/healthcheck1.wav
#cp audios/fax/02.wav /var/lib/asterisk/sounds/en/faxmachine/healthcheck2.wav
#cp audios/fax/03.wav /var/lib/asterisk/sounds/en/faxmachine/clearance1.wav
#cp audios/fax/04.wav /var/lib/asterisk/sounds/en/faxmachine/clearance2.wav
#cp audios/fax/05.wav /var/lib/asterisk/sounds/en/faxmachine/answers.wav
#cp audios/fax/tim.wav /var/lib/asterisk/sounds/en/faxmachine/tbl.wav
