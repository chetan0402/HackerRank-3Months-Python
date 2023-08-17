#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#


def fizzBuzz(n):
    div_by_3 = n % 3 == 0
    div_by_5 = n % 5 == 0
    if div_by_3 and div_by_5:
        print("FizzBuzz")
    elif div_by_3:
        print("Fizz")
    elif div_by_5:
        print("Buzz")

    if not div_by_5 and not div_by_3:
        print(n)


if __name__ == "__main__":
    n = int(input().strip())

    for i in range(1, n + 1):
        fizzBuzz(i)
