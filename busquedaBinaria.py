# -*- coding: utf-8 -*-
import random
from math import ceil
import sys

def binarySearch(numbers, numberToFind, low, high):
  if low > high:
    return False
  mid = (low + high) / 2
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

def selectionSort(A):
  # Traverse through all array elements
  for i in range(len(A)):
      # Find the minimum element in remaining
      # unsorted array
      min_idx = i
      for j in range(i+1, len(A)):
          if A[min_idx] > A[j]:
              min_idx = j
      # Swap the found minimum element with
      # the first element
      A[i], A[min_idx] = A[min_idx], A[i]
  return A

def run():
  l = 20
  numberArray = randomListArray(l)
  #print("Not sorted array")
  #print(numberArray)
  numbers = selectionSort(numberArray)
  #print("Sorted array")
  #print(numbers)
  numberToFind = int(raw_input("Input a number: "))
  result = binarySearch(numbers, numberToFind,0,(len(numbers)-1))
  if result is True:
    print('El numero SI esta en la lista')
  else:
    print('El numero NO esta en la lista')


if __name__ == '__main__':
    print('B U S Q U E D A  B I N A R I A')
    run()