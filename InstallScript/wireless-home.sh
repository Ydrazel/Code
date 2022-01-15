#! /bin/bash

#
# Script to establish wireless network connection.
#

systemctl start iwd &&
echo 'Starting iwd...' & sleep 2 &&
systemctl start dhclient@wlan0 &&
echo 'Starting dhclient...' & sleep 2 &&
iwctl station wlan0 connect 'NetMASTER Uydunet-49F0'
echo 'Connecting To Home Network...' & sleep 2 &&
echo 'Wireless Connection Established!'
