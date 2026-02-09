#!/usr/bin/env python3

try:
    num = int(input("Enter a number\n"))
    for i in range(0, 10):
        result = num * i
        print(f"{num} x {i} = {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")