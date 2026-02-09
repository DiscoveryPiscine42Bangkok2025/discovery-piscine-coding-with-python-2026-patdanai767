#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    word = sys.argv[1]
    word2 = sys.argv[2].split(" ")
    count = 0
    for w in word2:
        if w == word:
            count += 1
    print(count)
else:
    print("none")