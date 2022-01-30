#!/usr/bin/env bash

printf "setting up poglos (v1.0)\n"

sudo apt update -y
sudo apt upgrade -y

# from https://loganmarchione.com/2021/07/raspi-configs-mostly-undocumented-non-interactive-mode/
printf ""
sudo raspi-config nonint do_hostname poglos
sudo raspi-config nonint do_memory_split 16

printf iptables-persistent iptables-persistent/autosave_v4 boolean true | sudo debconf-set-selections
printf iptables-persistent iptables-persistent/autosave_v6 boolean true | sudo debconf-set-selections

sudo apt install vim python3-pip libsdl2-mixer-2.0-0 apache2 bridge-utils dnsmasq hostapd iptables-persistent -y

if [ "$(id -u)" != "0" ]; then
	printf "this must be run as root." 1>&2
	exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

copy_with_backup () {
	# If the destination file exists, back it up--but only if the backup file does not already exist
	if [ -f $2 ] && [ ! -f $2.-old ]; then
		mv -f ${2} ${2}.-old
	fi
	cp -f ${1} ${2}
}

# from https://learn.pimoroni.com/article/raspberry-pi-phat-dac-install
printf "setting up audio...\n"
sudo touch /etc/modprobe.d/rasp-blacklist.conf
sed -i -- 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/g' /etc/modprobe.d/rasp-blacklist.conf
sed -i -- 's/blacklist snd-soc-pcm512x/#blacklist snd-soc-pcm512x/g' /etc/modprobe.d/rasp-blacklist.conf
sed -i -- 's/blacklist snd-soc-wm8804/#blacklist snd-soc-wm8804/g' /etc/modprobe.d/rasp-blacklist.conf
sed -i -- 's/snd_bcm2835/#snd_bcm2835/g' /etc/modules

printf dtoverlay=hifiberry-dac >> /boot/config.txt
sed -i -- 's/dtparam=audio=on/#dtparam=audio=on/g' /boot/config.txt

copy_with_backup ${SCRIPT_DIR}/conf/asound.conf.ap /etc/.asound.conf
printf "done!\n\n"

printf "copying network config files...\n"
copy_with_backup ${SCRIPT_DIR}/conf/htaccess.ap /var/www/html/.htaccess
copy_with_backup ${SCRIPT_DIR}/conf/dnsmasq.conf.ap /etc/dnsmasq.conf
copy_with_backup ${SCRIPT_DIR}/conf/hostapd.conf.ap /etc/hostapd/hostapd.conf
copy_with_backup ${SCRIPT_DIR}/conf/br0.ap /etc/network/interfaces.d/br0
copy_with_backup ${SCRIPT_DIR}/conf/override.conf.ap /etc/apache2/conf-available/override.conf
copy_with_backup ${SCRIPT_DIR}/conf/rules.v4.ap /etc/iptables/rules.v4
printf "done!\n\n"

printf "modifying config files for ap...\n"
sed -i -- "s/^ssid=.*$/ssid=Poglos/g" /etc/hostapd/hostapd.conf
sed -i -- 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf
sed -i -- 's/ENABLED=0/ENABLED=1/g' /etc/default/dnsmasq
printf "done!\n\n"

printf "configuring apache...\n"
a2enconf override
a2enmod rewrite
printf "done!\n\n"

printf "installing python socket app...\n"
# pip install --upgrade --no-deps --force-reinstall ${SCRIPT_DIR}/ap
mkdir -p /home/pi/poglos
cp -r ${SCRIPT_DIR}/code/* /home/pi/poglos
pip install -r /home/pi/poglos/requirements.txt
printf "done!\n\n"

printf "configuring web interface...\n"
mkdir -p /var/www/html
cp -r ${SCRIPT_DIR}/www/* /var/www/html/
copy_with_backup ${SCRIPT_DIR}/conf/000-poglos.conf.ap /etc/apache2/sites-available/000-poglos.conf
a2dissite 000-default
a2ensite 000-poglos
printf "done!\n\n"

printf "setting up playback as service"
copy_with_backup ${SCRIPT_DIR}/conf/poglos.service /etc/systemd/system/
systemctl enable poglos
printf "done!\n\n"

printf "Disabling DHCP...\n"
update-rc.d dhcpcd disable
printf "done!\n\n"

printf "Enabling dnsmasq...\n"
systemctl enable dnsmasq
printf "done!\n\n"

printf "Enabling hostapd...\n"
systemctl unmask hostapd
systemctl enable hostapd
printf "done!\n\n"

printf "Disabling WPA Supplicant...\n"
cat > /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
EOF
printf "done!\n\n"

printf "All done!\n\n Reboot to apply changes.\n"
