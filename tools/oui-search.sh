#!/bin/bash

#set -x

VENDOR='Raspberry Pi'
OUI=`ip addr list | grep -w link | awk '{print $2}' | grep -P "^(?!00:00:00)"| grep -P "^(?!fe80)" | tr -d ":" | head -c 6`

if [[ $( curl -sS "http://standards-oui.ieee.org/oui.txt" | grep -i "$OUI" | grep -o "$VENDOR" ) = 'Raspberry Pi' ]]; then
        echo "This is a Pi"
else
        echo "This is NOT a Pi"
fi
