# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of numbers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that is random.

import time
import random
import os

# Your current working directory needs to see the AllSorts.py
# If you have issues you should comment out this line.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import AllSorts

# Run and time one sort
def runSort(sort_name, sort_function, numberTerms):
  print()
  print(sort_name)

  # Re-create the same lists for every sort so they are not already sorted
  orderedList = []
  reversedList = []
  randomList = []

  random.seed(2020)
  for i in range(numberTerms):
    orderedList.append(i)
    reversedList.insert(0, i)
    randomList.append(random.randint(1, 10000))

  startTime = time.time()
  sort_function(orderedList)
  endTime = time.time()
  print("Ordered list time:", endTime - startTime, "seconds")

  startTime = time.time()
  sort_function(reversedList)
  endTime = time.time()
  print("Reversed list time:", endTime - startTime, "seconds")

  startTime = time.time()
  sort_function(randomList)
  endTime = time.time()
  print("Random list time:", endTime - startTime, "seconds")

# Main function
def main():
  random.seed(2020)

  numberTerms = 10000

  # Keeping this part just like you had it
  orderedList = []
  reversedList = []
  randomList = []

  for i in range(numberTerms):
    orderedList.append(i)
    reversedList.insert(0, i)
    randomList.append(random.randint(1, 10000))

  print("Begin Sorting", numberTerms, "elements.")

  runSort("Bubble Sort", AllSorts.bubbleSort, numberTerms)
  runSort("Bubble Sort Early Exit", AllSorts.bubbleSortEarlyExit, numberTerms)
  runSort("Selection Sort", AllSorts.selectionSort, numberTerms)
  runSort("Insertion Sort", AllSorts.insertionSort, numberTerms)
  runSort("Merge Sort", AllSorts.mergeSort, numberTerms)

  print()
  print("Sorting Complete")

if __name__ == '__main__':
  main()