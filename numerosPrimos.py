# -*- coding: utf-8 -*-
from math import ceil
"""def is_prime(number):
    if number < 2:
        returnFalse
    elif number == 2:
        returnTrue
    elif number > 2 and number % 2 == 0:
        returnFalse
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                return False
    return True

def run():
    number = int(raw_input('Escribe un numero: '))
    result = is_prime(number)
    if result == True:
        print('El numero {} es un numero primo'.format(number))
    else: 
        print('El numero {} no es un numero primo'.format(number))"""


def run():
    numero = int(input("Ingrese un numero para saber si es primo: "))

    if primo(numero):
        print("El numero SI es primo")
    else:
        print("El numero ingresado NO es primo")

def primo(n):
    x = ceil((n / 2))
    while x > 1:
        if n % x == 0:
            return False
            break
        x = x - 1
    return True

if __name__ == '__main__':
    run()
