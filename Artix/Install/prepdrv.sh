#! /bin/bash

parted --script /dev/nvme0n1 \
	mklabel gpt \
	mkpart primary fat32 1MiB 256MiB \
	set 1 esp on \
	mkpart primary ext4 256MiB 100% \
quit &&

echo "Drive Preparation Successful!"
