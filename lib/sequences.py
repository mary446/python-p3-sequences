#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [0, 1]
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        while len(fib) < length:
            fib.append(fib[-1] + fib[-2])
        print(fib)