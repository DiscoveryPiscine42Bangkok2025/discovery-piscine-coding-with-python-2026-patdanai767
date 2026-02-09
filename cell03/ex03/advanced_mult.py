#!/usr/bin/env python3

import sys

mult = 0

if len(sys.argv) > 1:
    print("none")
else:
    for i in range(mult, 11):
        print(f"Table de {i}:",end="")
        for j in range(0, 11):
            print(f" {i*j}",end="")
        print("")
