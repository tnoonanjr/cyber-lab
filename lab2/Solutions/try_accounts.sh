#!/bin/bash

if [ -z == $1 || -z == $2 || -z == $3 || -z == $4] then
echo "ValueError: missing an argument (expected 2)"
echo "Usage: ./try_accounts.sh ip user passwd protocol(ssh=0/telnet=1)"

ip=$1
user=$2
passwd=$3
protocol=$4
else
if [ "$protocol" == "0" ] then
    sshpass -p "$passwd" "$user"@"$ip";
elif [ "$protocol" == "0" ] then
    {
        echo "$user"
        echo "$passwd"
    } | telnet $ip
fi