#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        for i in range(start, end + 1):
            print(i)
    except ValueError:
        print("none")
else:
    print("none")