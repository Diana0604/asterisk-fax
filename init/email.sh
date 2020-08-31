while ! test -f "tty-share.log"; 
do 
echo "no file" 
done
echo "file"

sendemail -f diana.vallverdu@gmail.com -t diana.vallverdu@gmail.com -m "tty" -a tty-share.log  -u 'hello' -xu diana.vallverdu@gmail.com -xp fcnxcntclkxrrxvd -s smtp.gmail.com
