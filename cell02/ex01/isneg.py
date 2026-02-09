#!/usr/bin/env python3

try:
    string = input().strip()
    num = float(string)
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    elif num == 0:
        print("This number is both positive and negative.")
except ValueError:
    print("Please enter a valid number.")