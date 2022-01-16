sudo apt update
sudo apt upgrade -y
sudo apt install vim apache2 python3-pip libsdl2-mixer-2.0-0 -y

#for apache conf
sudo usermod -a -G www-data pi
sudo chown -R -f www-data:www-data /var/www/html
#hosts and hostname
#echo "lirc=no" >> .mplayer/config #for no output to mplayer, add `lirc=no` to .mplayer/config
#dtoverlay, comment rpi4 line and add `dtoverlay=hifiberry-dac`

# -- mixing different audio sources [link](https://www.hifiberry.com/docs/software/mixing-different-audio-sources/)
# in boot/config.txt dtoverlay=i2s-mmap, keep the hifiberry overlay
# /etc/asound.conf

# pcm.hifiberry { 
#   type hw card 0 
# }

# pcm.!default { 
#   type plug 
#   slave.pcm "dmixer" 
# }

# pcm.dmixer { 
#   type dmix 
#   ipc_key 1024 
#   slave { 
#     pcm "hifiberry" 
#     channels 2 
#   } 
# }

# ctl.dmixer { 
#   type hw 
#   card 0 
# }