#!/usr/bin/env python3

try:
    fir_num = int(input("Enter the first number:\n"))
    sec_num = int(input("Enter the second number:\n"))

    result = fir_num * sec_num
    print(fir_num, "x" , sec_num, "=", result)

    if result < 0:
        print("The result is negative.")
    elif result > 0:
        print("The result is positive.")
    else:
        print("The result is positive and negative.")
except:
    print("Invalid input. Please enter numeric values.")