#!/usr/bin/env python3

try:
    num = int(input("Enter a number less than 25\n"))
    for i in range(num, 26):
        print("Inside the loop, my variable is ",i)
except ValueError:
    print("Invalid input. Please enter a valid number.")