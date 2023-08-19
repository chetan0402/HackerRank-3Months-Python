#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    binary = bin(n).replace("0b", "")
    binary = ("0" * (32 - len(binary))) + binary
    binary = list(binary)
    i = 0
    for bit in binary:
        if bit == "1":
            binary[i] = "0"
        if bit == "0":
            binary[i] = "1"
        i += 1

    return int("".join(binary), 2)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + "\n")

    fptr.close()
