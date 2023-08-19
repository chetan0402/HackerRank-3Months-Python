#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    # Write your code here
    lenght = len(s)
    og_msg = "SOS" * int(lenght / 3)
    s = list(s)
    og_msg = list(og_msg)
    i = 0
    error_count = 0
    while i < lenght:
        if not s[i] == og_msg[i]:
            error_count += 1
        i += 1

    return error_count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + "\n")

    fptr.close()
