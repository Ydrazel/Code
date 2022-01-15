#! /bin/bash

mkfs.vfat -n esp /dev/nvme0n1p1 &&
mkfs.f2fs -l arch -O extra_attr,inode_checksum,sb_checksum,compression /dev/nvme0n1p2 &&

echo "Successfully Formatted Filesystems.."
