#!/usr/bin/env python3

def print_fibonacci(length):
    i = 0
    current = 0
    fib_list = []

    while i < length:
        fib_list.append(current)
        if current == 0:
            current = 1
        else: 
            current = current + fib_list[i - 1]
        i += 1
    
    print(fib_list)