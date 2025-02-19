#!/bin/bash

if [ "" == "$1" ]
then
echo "ValueError: missing 1 argument"
echo "Usage: ./try_ports.sh [ip address]"

else
for byte in `seq 1 254`; do
# Test the port and print the line if it connects
#ssh -o ConnectTimeout=1 $1"."$byte # | grep -h "Connected to" &
telnet -w 1 $1"."$byte
done
fi