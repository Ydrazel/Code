#!/bin/bash

# Settings Available Under Systemd ############################################
#echo "vm.dirty_writeback_centisecs = 6000" > /etc/sysctl.d/dirty.conf &&
#echo "vm.laptop_mode = 5" > /etc/sysctl.d/laptop.conf &&

# Module Settings #############################################################
echo -e "options snd_hda_intel power_save=1\noptions snd_ac97_codec power_save=1" > /etc/modprobe.d/audio_powersave.conf &&

# Udev Rules ##################################################################
echo 'SUBSYSTEM=="pci", ATTR{power/control}="auto"' > /etc/udev/rules.d/pci_pm.rules &&

echo 'ACTION=="add", SUBSYSTEM=="net", KERNEL=="wl*", RUN+="/usr/bin/iw dev $wlan0 set power_save on"' > /etc/udev/rules.d/81-wifi-powersave.rules &&

echo 'ACTION=="add", SUBSYSTEM=="usb", TEST=="power/control", ATTR{power/control}="auto"' > /etc/udev/rules.d/50-usb_power_save.rules &&

echo 'ACTION=="add", SUBSYSTEM=="scsi_host", KERNEL=="host*", ATTR{link_power_management_policy}="med_power_with_dipm"' > /etc/udev/rules.d/hd_power_save.rules &&

echo 'SUBSYSTEM=="rfkill", ATTR{type}=="bluetooth", ATTR{state}="0"' > /etc/udev/rules.d/50-bluetooth.rules &&

echo 'KERNEL=="card0", SUBSYSTEM=="drm", DRIVERS=="amdgpu", ATTR{device/power_dpm_force_performance_level}="low"' > /etc/udev/rules.d/30-amdgpu-pm.rules &&

echo 'KERNEL=="card0", SUBSYSTEM=="drm", DRIVERS=="amdgpu", ATTR{device/power_dpm_state}="battery"' > /etc/udev/rules.d/30-amdgpu-dpm.rules &&

# Device FS Entries ###########################################################
echo "auto" | sudo tee /sys/bus/pci/devices/0000\:05\:00.0/ata1/power/control &&
echo "auto" | sudo tee /sys/bus/pci/devices/0000\:05\:00.1/ata2/power/control &&
echo "powersave" | sudo tee /sys/module/pcie_aspm/parameters/policy
echo "low" | sudo tee /sys/class/drm/card0/device/power_dpm_force_performance_level
