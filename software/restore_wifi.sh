#!/usr/bin/env bash

if [ "$(id -u)" != "0" ]; then
	echo "This must be run as root." 1>&2
	exit 1
fi

# Get the script folder
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Enter SSID of WiFi network to which to connect:"
read SSID

echo "Enter WiFi Password:"
read PSK

echo "Copying config files..."
rm -f ${SCRIPT_DIR}/cfg/interfaces.d/br0
cp -f ${SCRIPT_DIR}/cfg/rules.v4.wifi /etc/iptables/rules.v4
echo "done!"

echo "Modifying config files..."
sed -i -- 's/net.ipv4.ip_forward=1/#net.ipv4.ip_forward=1/g' /etc/sysctl.conf
sed -i -- 's/DAEMON_CONF="\/etc\/hostapd\/hostapd.conf"/#DAEMON_CONF=""/g' /etc/default/hostapd
sed -i -- 's/ENABLED=1/ENABLED=0/g' /etc/default/dnsmasq
echo "done!"

echo "Enable DHCP..."
update-rc.d dhcpcd enable
echo "done!"

echo "Disable dnsmasq..."
systemctl disable dnsmasq
echo "done!"

echo "Disable hostapd..."
systemctl disable hostapd
systemctl mask hostapd
echo "done!"

cat > /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
    ssid="${SSID}"
    psk="${PSK}"
}
EOF

echo "All done! Reboot to apply changes."
