#! /bin/bash

findmnt -no UUID -T /swapfile &&
filefrag -v /swapfile | awk '{ if($1=="0:"){print substr($4, 1, length($4)-2)} }' &&
echo "These are the values for the kernel paramaters."
