# asterisk-fax
Config for. A fax telephony system using asterisk for scape-room style shit
# What you'll need
- Raspberry PI
- SD card
- 12V (?) connector for PI
- ATA (Grandstream, Linksys...) -> I have listed how to config the ones I have used and normally it's pretty similar from brand to brand
- Install asterisk: Follow http://www.raspberry-asterisk.org/ instructions
- If you don't have access to wireless internet: USB Dongle + SIM with data
# Installation
## Step 1: Turn raspberry into ehternet router 
- If you don't have wireless access to internet: Install USB dongle (TODO)
- Follow https://linuxhint.com/raspberry_pi_wired_router/ instructions
- Do *NOT* activate firewall (TODO -> CHECK)
## Step 2: Set up hardware
- Connect ethernet cable from pi to grandstream pbx in the Global Network pin
- Connect fax machine from extension #2
## Step 2: Configure freepbx correctly (TODO write the proper stuffff)
- Go to Extensions -> Add new PJSIP Extension and add Extensions 1000, 2000, 3000 (1000 can be used from extension #1 and 3000 can be used from computer for ex.)
- Go to that thing that detects the network
- blablalba
## Step 3: Configure an ATA to be used with your raspberry
### Grandstream
### Linksys
TODO
