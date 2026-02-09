#!/usr/bin/env python3

import sys

def shrink(str):
    return str[:8]

def enlarge(str):
    if len(str) < 8:
        str += 'Z' * (8 - len(str))
    return str
    
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        shrinked = shrink(arg)
        enlarged = enlarge(shrinked)
        print(enlarged)
else:
    print("none")