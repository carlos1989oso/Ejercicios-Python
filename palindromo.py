# -*- coding: utf-8 -*-

def palindrome(word):
    if word[::-1] == word:
        return True

def run():
    word = str(raw_input('Escribe la palabra: '))
    if palindrome(word):
        print('La palabra {} es un palindromo'.format(word))
    else:
        print('La palabra {} no es un palindromo'.format(word))

if __name__ == '__main__':
    run()
