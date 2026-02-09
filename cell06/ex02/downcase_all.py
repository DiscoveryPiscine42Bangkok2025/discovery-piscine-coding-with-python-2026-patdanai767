#!/usr/bin/env python3

import sys

def downcase_all(str):
    return str.lower()

if len(sys.argv) > 1:
    print("\n".join([downcase_all(arg) for arg in sys.argv[1:]]))
else:
    print("none")