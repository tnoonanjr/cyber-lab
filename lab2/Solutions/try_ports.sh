#!/bin/bash

if [ "" == "$1" ]
then
echo "ValueError: missing 1 argument"
echo "Usage: ./try_ports.sh [ip address]"

else
for port in `seq 1 254`; do
# Test the port and print the line if it connects
nc -zv -w 1 $1 $port 2>&1 | grep succeeded &
done
fi