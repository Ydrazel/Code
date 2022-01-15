#! /bin/bash

basestrap /mnt base base-devel s6-base elogind-s6 f2fs-tools iw&&
basestrap /mnt linux-zen linux-tools-meta linux-firmware &&

echo "Base System Installation Complete!" &&

fstabgen -U /mnt >> /mnt/etc/fstab &&

echo "fstab File Generation Complete!"
