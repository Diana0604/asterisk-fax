rm /var/lib/asterisk/sounds/en/faxmachine/eastereggs/*
rmdir /var/lib/asterisk/sounds/en/faxmachine/eastereggs
rm /var/lib/asterisk/sounds/en/faxmachine/*
cp -r /fax/sounds/fax/* /var/lib/asterisk/sounds/en/faxmachine/
#cp -r /fax/sounds/fax/easter_eggs /var/lib/asterisk/sounds/en/faxmachine/