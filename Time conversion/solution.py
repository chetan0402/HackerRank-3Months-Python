#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    if s[0:2] == "12" and s[-2] == "A":
        return f"00:{s[3:8]}"
    if s[0:2] == "12" and s[-2] == "P":
        return f"12:{s[3:8]}"
    past_12 = s[-2] == "P"
    time_split = s[0:-2].split(":")
    to_return = ""
    if past_12:
        to_return = str(int(time_split[0]) + 12)
    else:
        to_return = time_split[0]
    to_return = f"{to_return}:{time_split[1]}:{time_split[2]}"
    return to_return


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
