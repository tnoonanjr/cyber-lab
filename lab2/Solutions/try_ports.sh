#!/bin/bash

if [ " " == "$1" ]
then
echo "ValueError: missing 1 argument"
echo "Usage: ./try_ports.sh [3 bytes of ip address]"

else
for port in `seq 1 65535`; do
# Test the port and print the line if it connects
telnet -z $1 port | grep -h "Connected to" &
done
fi