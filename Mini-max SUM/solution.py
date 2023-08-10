#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    print(f"{arr[0]+arr[1]+arr[2]+arr[3]} {arr[1]+arr[2]+arr[3]+arr[4]}")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
