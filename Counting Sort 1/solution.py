#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    count_arr = []
    for _ in range(0, 100):
        count_arr.append(0)

    i = 0
    while i < len(arr):
        count_arr[arr[i]] += 1
        i += 1

    return count_arr


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
