import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for element in arr:
        if element > 0:
            positive_count += 1
        if element < 0:
            negative_count += 1
        if element == 0:
            zero_count += 1
    print(positive_count / len(arr))
    print(negative_count / len(arr))
    print(zero_count / len(arr))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
