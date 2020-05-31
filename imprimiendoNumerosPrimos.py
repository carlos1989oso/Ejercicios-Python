# -*- coding: utf-8 -*-
from math import ceil

def prime_print(number):
    j = 0
    i = 1
    lists = []
    while j <= number:  
        if is_prime(i):
              print(i)
              j = j + 1
        i = i + 1


def is_prime(number):
    x = ceil((number / 2))
    while x > 1:
        if number % x == 0:
            return False
            break
        x = x - 1
    return True

def run():
    number = int(raw_input('cuantos numeros primos quieres imprimir: '))
    prime_print(number)

if __name__ == '__main__':
    run()
