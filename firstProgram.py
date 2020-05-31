# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    movement = turtle.Turtle()
    make_square(movement)

def make_square(movement):
    sum = int(raw_input('Tamaño de cuadrado: '))
    length = 1
    #sum = int(10)
    for i in range(100):
        make_line_and_turn(movement, length)
        length = length + sum


def make_line_and_turn(movement, length):
    movement.forward(length)
    movement.left(90)


if __name__ == '__main__':
    main()

turtle.mainloop()