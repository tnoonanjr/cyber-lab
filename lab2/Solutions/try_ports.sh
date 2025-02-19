#!/bin/bash

if [ "" == "$1" ]
then
echo "ValueError: missing 1 argument"
echo "Usage: ./try_ports.sh [ip address]"

else
for ip in `seq 1 254`; do
# Test the port and print the line if it connects
ssh $1.$ip | telnet $1.ip | grep succeeded 1 > open_ssh_telnet.log
done
fi