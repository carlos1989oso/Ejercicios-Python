# -*- coding: utf-8 -*-
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('----- * ----- * ----- * ----- * -----')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    word_summary = []
    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una letra: '))

        try:
            word_summary.index(current_letter)
            print('')
            print('Ya has escogido la letra {}, intenta de nuevo'.format(current_letter))
            print('')
        except ValueError:
            word_summary.append(current_letter)

            letter_indexes = []
            for idx in range(len(word)):
                if word[idx] == current_letter:
                    letter_indexes.append(idx)

            if len(letter_indexes) == 0:
                tries += 1
                if tries == 7:
                    display_board(hidden_word, tries)
                    print('')
                    print('!has perdido¡...La palabra era {}'.format(word))
                    break
            else:
                for idx in letter_indexes:
                    hidden_word[idx] = current_letter
                letter_indexes = []

            try:
                hidden_word.index('-')
            except ValueError:
                print('')
                print('!Has ganado¡...la palabra es: {}'.format(word))
                break
        

    pass

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
