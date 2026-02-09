#!/usr/bin/env python3

try:
    age = int(input("Please tell me your age: "))
    if age < 0:
        print("You entered a negative age. Please enter a valid age.")
    else:
        if age == 1:
            print(f"You are currently {age} year old.")
        else:
            print(f"You are currently {age} years old.")
        for i in range(1,4):
            print(f"In {i*10} years, you'll be {age + (i*10)} years old.")
except ValueError:
    print("Invalid input. Please enter a valid age.")


