sudo chown -R diana: /var/{lib,log,run,spool}/asterisk /usr/lib/asterisk /etc/asterisk
 
sudo chmod -R 750 /var/{lib,log,run,spool}/asterisk /usr/lib/asterisk /etc/asterisk

asterisk -rx 'core stop now'

mv /var/lib/asterisk/astdb.sqlite3 /tmp

asterisk
