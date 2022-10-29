#!/usr/bin/python3


def even_or_odd(number):
    result = number % 2

    if result == 0:
        print('The number', number, 'is odd')
    else:
        print('The number', number, 'is even')

def main():
    num = int(input('Type a number: '))
    even_or_odd(num)

if __name__ == "__main__":
    main()