#!/usr/bin/env python3

import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: log_parser.py <log_file>")
    sys.exit(1)

log_file = sys.argv[1]

ip_counter = Counter()

with open(log_file, 'r') as file:
    for line in file:
        try:
            ip = line.split()[0]
            ip_counter[ip] += 1
        except IndexError:
            #  empty line
            pass

for ip, count in ip_counter.most_common():
    print(f"{ip}: {count}")
