#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    count = 0

    i1 = 0
    while i1 < n:
        i2 = i1 + 1
        while i2 < n:
            if (ar[i1] + ar[i2]) % k == 0:
                count += 1
            i2 += 1
        i1 += 1

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
