
#!/bin/sh

#run this script from /etc/rc.local with the command sh /fax/reboot.sh

#/usr/bin/cvlc /fax/audios/speaker/00-arrival.mp3 > /dev/null 2>&1 & 

#/usr/bin/cvlc /fax/audios/speaker/01-breathing.mp3 > /dev/null 2>&1 & 

amixer set 'Headphone' 100%
python /fax/python/main.py
