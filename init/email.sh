while ! test -f "/tmp/${temptty}-tty-share.log";
do 
echo "no file" 
done
echo "file"

#echo "looking in : /tmp/${temptty}-tty-share.log"

sendemail -f diana.vallverdu@gmail.com -t diana.vallverdu@gmail.com -m "tty" -a "/tmp/${temptty}-tty-share.log"  -u 'hello' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com
