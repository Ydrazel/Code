dd if=/dev/zero of=/mnt/swapfile bs=1M count=4000 status=progress &&
chmod 600 /mnt/swapfile &&
mkswap /mnt/swapfile &&
swapon /mnt/swapfile &&
echo "Swap File Successfully Generated!"
