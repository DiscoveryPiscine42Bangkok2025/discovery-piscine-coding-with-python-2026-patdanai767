#!/usr/bin/env python3

try:
    num = float(input("Give me a number: "))
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a float.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
