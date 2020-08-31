
#!/bin/sh

#run this script from /etc/rc.local with the command sh /fax/reboot.sh

#/usr/bin/cvlc /fax/audios/speaker/00-arrival.mp3 > /dev/null 2>&1 & 

#/usr/bin/cvlc /fax/audios/speaker/01-breathing.mp3 > /dev/null 2>&1 & 

amixer set 'Headphone' 100%

#python /fax/python/main.py
#initial vs main

wget -q --spider http://google.com 
while ! [ $? -eq 0 ] 
do 
echo "Offline" 
done
echo "Online"

python /fax/python/reboot.sh &

rm tty-share.log

sh /fax/init/email.sh &

/tty-share/tty-share.rpi -logfile tty-share.log
