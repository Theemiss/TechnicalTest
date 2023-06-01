#!/usr/bin/bash

source=$1
max_backups=$2
dest=$3
naming_pattern="backup_$(date +%Y%m%d%H%M%S).tar.gz"
echo "Usage: archive.sh <source> <max_backups> <dest>"
if [ ! -d $source ]; then
    echo "source $source not found"
    exit 1
fi
if [ ! -d $dest ]; then
    echo "dest $dest not found"
    exit 1
fi
# check if max_backups is a positive number
if ! [[ $max_backups =~ ^[0-9]+$ ]]; then
    echo "max_backups is not a number: $max_backups"
    if [ -z $max_backups ]; then
        max_backups=5
        echo "using default value: $max_backups"
    fi
elif [ $max_backups -lt 0 ]; then
    echo "max_backups is negative: $max_backups"
    exit 1
fi


tar -czf "${dest}/${naming_pattern}" -C "${source}" .

backup_count=$(ls -t "${dest}" | grep -c "^backup_")
if [ $backup_count -gt $max_backups ]; then
  excess_backups=$((backup_count - max_backups))
  ls -t "${dest}" | grep "^backup_" | tail -n $excess_backups | xargs -I {} rm "${dest}/{}"
fi