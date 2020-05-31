# -*- coding: utf-8 -*-

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a pesos colombianos y viceversa.')
    print('')
    print('1. Pesos mexicanos a colombianos')
    print('2. Pesos colombianos a mexicanos')
    print('')
    selection = int(raw_input())

    if selection == 1:
        ammount = float(raw_input('ingresa la cantidad de pesos mexicanos que quieres covertir: '))
        result = foreign_exchange_calculator(ammount)
    elif selection == 2:
        ammount = float(raw_input('ingresa la cantidad de pesos colombianos que quieres covertir: '))
        result = colombian_to_mexican(ammount)
    else:
        print('No es posible acceder al tipo cambio')
    print('$ {} pesos colombianos son $ {} pesos mexicanos'.format(ammount,result))
    print('')

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount

def colombian_to_mexican(ammount):
    mex_to_col_rate = 145.97
    return ammount/mex_to_col_rate

if __name__ == '__main__':
    run()
