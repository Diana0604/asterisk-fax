# asterisk-fax
Config for. A fax telephony system using asterisk for scape-room style shit

BACKUP:` sudo dd if=/dev/diskN bs=4m | pv | dd of=name.img bs=4m`

where diskN has to be replaced by the external disk and name by the name you desire

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
### First configs - Raspberry
- Enter with user root, password raspberry
- raspi-config -> Advanced Options -> Expand Filesystem -> reboot
- regen-hostkeys
- configure-timezone
-dpkg reconfigure-locales-> all -> en_GB
- raspbx-upgrade
### First configs - FreePBX
From a computer that is connected to the same network as pi:
- Open browser
- Go to raspbx.local
#### Add extensions
- Applications -> Extensions
-Add Extension -> Add new extension (pjspi) -> Choose User Extension/Display Name and Secret
### Activate NAT & FAX
- Settings -> Asterisk SIP Settings
- In NAT Settings section -> Detect Network Settings
- In T38 Pass-Through select YES

Once all is done Apply Config
## Step 2: Connect to your pi
There are two ways to connect to your newly installed asterisk!
### Option 1 (preferred): SSH
- Connect pi to internet through ethernet - It has to be the same 
### Option 2: Directly
## Step 1: Turn raspberry into ehternet router 
### Configure the network
- If you don't have wireless access to internet: Install USB dongle (TODO)
- `sudo nano /etc/network/interfaces.d/wlan0`
In this file, add code: 
    ```
    allow-hotplug wlan0
    iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    ```
- `sudo nano /etc/network/interfaces.d/eth0`
In this file, add code: 
    ```
    auto eth0
      iface eth0 inet static
      address 192.168.100.1
      netmask 255.255.255.0
    ```
- `sudo systemctl disable dhcpcd`
- `sudo reboot`
-Now check ` ip addr show eth0` gives you `192.168.100.1`
### Configure DHCDP
- `sudo apt update'
- `sudo apt install isc-dhcp-server`. Don't worry if you see a red alarming `Active: failed`. We have not configured dhcdp so it's ok.
- `sudo nano /etc/dhcp/dhcpd.conf`. In this file: 
```
TODO
```
- `sudo nano /etc/default/isc-dhcp-server`, in that file, modify appropriate line for:
    ```
    INTERFACESV4="eth0"
    ```
- `sudo reboot`
- `sudo systemctl status isc-dhcp-server` should be running
(All taken from Follow https://linuxhint.com/raspberry_pi_wired_router/ instructions )
- Do *NOT* activate firewall (TODO -> CHECK)
## Step 2: Set up hardware
- Connect ethernet cable from pi to grandstream pbx in the Global Network pin
- Connect fax machine from extension #2
## Step 2: Configure freepbx correctly (TODO write the proper stuffff)
- Go to Extensions -> Add new PJSIP Extension and add Extensions 1000, 2000, 3000 (1000 can be used from extension #1 and 3000 can be used from computer for ex.)
- Go to that thing that detects the network
- blablalba
## AUDIO
`/usr/bin/vlc /fax1/audios/xx.wav `
## Execute on boot
`nano /etc/rc.local `
## Step 3: Configure an ATA to be used with your raspberry
### Grandstream
### Linksys
TODO

### TODO: reboot script
