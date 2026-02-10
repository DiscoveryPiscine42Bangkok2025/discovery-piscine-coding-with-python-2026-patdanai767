#!/usr/bin/env python3

import sys

mult = 0

if len(sys.argv) > 1:
    print("none")
else:
    while mult < 11:
        print(f"Table de {mult}:",end="")
        j = 0
        while j < 11:
            print(f" {mult*j}",end="")
            j += 1
        print("")
        mult += 1

