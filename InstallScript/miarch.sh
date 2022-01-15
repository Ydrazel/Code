#! /bin/bash

loadkeys trq &&
iwctl station wlan0 connect 'NetMASTER Uydunet-49F0' &&
timedatectl set-ntp true &&

# Partitioning the drive ######################################################

parted --script /dev/nvme0n1 \
	mklabel gpt \
	mkpart primary fat32 1MiB 512MiB \
	set 1 esp on \
	mkpart primary ext4 512MiB 100% \
quit &&

# Formatting Partitions #######################################################

mkfs.vfat -n esp /dev/nvme0n1p1 &&
mkfs.f2fs -l arch -O extra_attr,inode_checksum,sb_checksum,compression /dev/nvme0n1p2 &&

# Mounting Partitions #########################################################

mount /dev/nvme0n1p2 /mnt &&
mkdir -p /mnt/boot &&
mount /dev/nvme0n1p1 /mnt/boot &&

# Creating and Mounting Swapfile ##############################################

dd if=/dev/zero of=/mnt/swapfile bs=1M count=4000 status=progress &&
chmod 600 /mnt/swapfile &&
mkswap /mnt/swapfile &&
swapon /mnt/swapfile &&

# Installing Base System ######################################################

pacstrap /mnt base base-devel linux linux-firmware sof-firmware amd-ucode man-db man-pages texinfo iwd dhclient f2fs-tools vi vim xdg-user-dirs xdg-utils xdg-dbus-proxy fish git gnome gnome-tweaks firefox gimp libreoffice &&

# Copying Installation Script and Configuration Files to New System ###########

cp -r /InstallScript /mnt/

# System Configuration ########################################################

genfstab -U /mnt >> /mnt/etc/fstab &&
arch-chroot /mnt ln -sf /usr/share/zoneinfo/Europe/Istanbul /etc/localtime &&
arch-chroot /mnt hwclock --systohc &&
arch-chroot /mnt echo -e "en_US.UTF-8 UTF-8 \ntr_TR.UTF-8 UTF-8" > /etc/locale.gen &&
arch-chroot /mnt locale-gen &&
arch-chroot /mnt echo "LANG=en_US.UTF-8" > /etc/locale.conf &&
arch-chroot /mnt echo "KEYMAP=trq" > /etc/vconsole.conf &&
arch-chroot /mnt echo "kuz" > /etc/hostname &&
arch-chroot /mnt echo -e "127.0.0.1		localhost\n::1	localhost\n127.0.1.1		kuz.arch	kuz" > /etc/hosts &&
arch-chroot /mnt echo "blacklist	pcspkr" > /etc/modprobe.d/blacklist-pcspkr.conf &&
arch-chroot /mnt mkinitcpio -P &&
arch-chroot /mnt passwd &&
arch-chroot /mnt useradd -m -G wheel -s /bin/fish owl &&
arch-chroot /mnt passwd owl &&
arch-chroot /mnt bootctl install &&
arch-chroot /mnt cp /InstallScript/entries/* /boot/loader/entries/ &&
arch-chroot /mnt bootctl status &&
arch-chroot /mnt systemctl enable gdm &&

# Unmounting The Drives and Finalizing Installation ###########################

umount -R /mnt &&
echo "Installation Complete! Please Reboot The System."
