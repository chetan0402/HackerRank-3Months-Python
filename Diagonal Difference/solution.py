#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    number_of_rows_and_colums = len(arr)
    num1 = 0
    num2 = 0
    for i in range(0, number_of_rows_and_colums):
        num1 += arr[i][i]
        num2 += arr[i][number_of_rows_and_colums - i - 1]
    return abs(num1 - num2)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
