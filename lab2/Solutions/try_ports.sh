#!/bin/bash

if [ "" == "$1" ]
then
echo "ValueError: missing 1 argument"
echo "Usage: ./try_ports.sh [ip address]"
else

    log_ssh = "open_ssh.log"
    log_telnet = "open_telnet.log"
    > "$log_ssh"
    > "$log_telnet"

    for last_byte in $(seq 1 254); do
    # Test the port and print the line if it connects
        if  nc -zv -w 1 $1.$last_byte 22 then
            echo "$1.$last_byte\n" >> "$log_ssh"
        fi

        if nc -zv -w 1 $1.$last_byte 23
            echo "$1.$last_byte\n" >> "$log_telnet"
        fi
    
    done
fi