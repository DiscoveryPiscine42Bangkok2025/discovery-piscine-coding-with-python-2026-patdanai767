#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    s = sys.argv[1]
    if "z" in s:
        for z in s:
            if z == "z":
                print("z", end="")
    else:
        print("none")
else:
    print("none")