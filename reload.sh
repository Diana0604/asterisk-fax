#asterisk 
cp extensions_custom.conf /etc/asterisk/extensions_custom.conf
asterisk -rx 'dialplan reload'

