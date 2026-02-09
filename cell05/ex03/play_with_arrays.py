#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

print(arr)

for i in range(len(arr)):
    arr[i] += 2
    if arr[i] > 5:
        new_set.add(arr[i])

print(new_set)

