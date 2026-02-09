#!/usr/bin/env python3
    
try:
    first_num = int(input("Give me the first number: "))
    second_num = int(input("Give me the second number: "))

    print("Thank you!")
    print(f"{first_num} + {second_num} = {first_num + second_num}")
    print(f"{first_num} - {second_num} = {first_num - second_num}")
    print(f"{first_num} / {second_num} = {first_num / second_num}")
    print(f"{first_num} * {second_num} = {first_num * second_num}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
