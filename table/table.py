#!/usr/bin/python3


def table():
    num = 0
    choice = int(input('Type a number: '))
    while num < 10:
        num = num+1
        result = choice * num
        print(f'{choice} x {num} = {result}')

table()