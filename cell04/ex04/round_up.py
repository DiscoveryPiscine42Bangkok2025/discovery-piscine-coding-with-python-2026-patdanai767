#!/usr/bin/env python3

try:
    num = float(input("Give me a number: "))
    rounded = int(round(num))
    if num > rounded and num > 0:
        print(rounded + 1)
    else:
        print(rounded)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
