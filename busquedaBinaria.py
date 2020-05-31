# -*- coding: utf-8 -*-
import random
from math import ceil
import sys

def binarySearch(numbers, numberToFind, low, high):
  if low > high:
    return False
  mid = (low + mid) / 2
  if numbers[mid] == numberToFind:
    return True
  elif numbers[mid] > numberToFind:
    return binarySearch(numbers,numberToFind,low, mid-1)
  else:
    return binarySearch(numbers,numberToFind,mid + 1,high)

def randomListArray(n):
      arrayList = [0]  * n
      for i in range(n):
          arrayList[i] = random.randint(0, 100)
      return arrayList

def selectionSort(array):
  #recorremos los numeros en el array
  for i in range(len(array)):
    #Encontramos el valor minimo
    minValue = i
    for j in range(i+1, len(array)):
      if array[minValue] > array[j]:
        minValue=j
      array[i], array[minValue] = array[minValue], array[i]
  return array

def run():
  l = 20
  numberArray = randomListArray(l)
  print("Not sorted array")
  print(numberArray)
  numberArray = selectionSort(numberArray)
  print("Sorted array")
  print(numberArray)

  numberToFind = int(rawInput('Input a number: '))
  result = binarySearch(numberArray, numberToFind,0,(len(numberArray-1)))
  if result is True:
    print('El numero SI esta en la lista')
  else:
    print('El numero NO esta en la lista')


if __name__ == '__main__':
    print('B U S Q U E D A  B I N A R I A')
    run()