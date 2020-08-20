# asterisk-fax
Config for. A fax telephony system using asterisk for scape-room style shit
# What you'll need
## Basics
- Raspberry PI - I used Model 4B
- SD card - 16GB <= size <= 64GB
- Appropriate Power Supply - (3.0A for Model 4B)
## Connect to pi

- ATA (Grandstream, Linksys...) -> I have listed how to config the ones I have used and normally it's pretty similar from brand to brand
- Optional (if you want to have portable system): USB Dongle + SIM with data TODO: which dongles work?
# Installation
## Step 1: Install asterisk
The first thing to do is install asterisk.
- Download newest image from http://www.raspberry-asterisk.org/downloads/ (at the time of this project I used *RasPBX images based on Raspbian 10 Buster*)
- Connect SD card to your computer
- Install OS into SD card. You can find instructions in section *Writing the image* of https://www.raspberrypi.org/documentation/installation/installing-images/
- Boot your raspberry pi
## Step 2: Connect to your pi
There are two ways to connect to your newly installed asterisk!
### Option 1 (preferred): SSH
- Connect pi to internet through ethernet - It has to be the same 
### Option 2: Directly
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
## AUDIO
/usr/bin/vlc /fax1/audios/xx.wav 
nano /etc/rc.local 
## Step 3: Configure an ATA to be used with your raspberry
### Grandstream
### Linksys
TODO

### TODO: reboot script
