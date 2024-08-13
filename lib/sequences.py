#!/usr/bin/env python3

def print_fibonacci(length):
    list = [0, 1]

    while len(list) < length:
        new_number = list[-1] + list[-2]
        list.append(new_number)

    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        print(list)

print_fibonacci(1)
