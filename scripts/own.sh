asterisk -rx 'core stop now'

mv /var/lib/asterisk/astdb.sqlite3 /tmp

asterisk

sleep 5

chown -R diana: /var/{lib,log,run,spool}/asterisk /usr/lib/asterisk /etc/asterisk
 
chmod -R 750 /var/{lib,log,run,spool}/asterisk /usr/lib/asterisk /etc/asterisk

sleep 5

asterisk