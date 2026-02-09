#!/usr/bin/env python3

def array_of_names(persons_dict):
    result = []
    for keys, values in persons_dict.items():
        keys = keys.capitalize()
        values = values.capitalize()
        result.append(f"{keys} {values}")
    return result
        


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))