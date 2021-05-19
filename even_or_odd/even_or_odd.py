#!/usr/bin/python3


def even_or_odd():
    num = int(input('Type a number: '))
    result = num % 2

    if result == 0:
        print('The number', num, 'is odd')
    else:
        print('The number', num, 'is even')

even_or_odd()