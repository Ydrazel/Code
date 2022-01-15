#! /bin/bash

mount /dev/nvme0n1p2 /mnt &&
mkdir -p /mnt/boot &&
mount /dev/nvme0n1p1 /mnt/boot &&

echo "Partitions Mounted.."
