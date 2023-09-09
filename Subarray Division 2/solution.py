#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    to_return=0
    lenS=len(s)
    tracker=[]
    for i1 in range(0,m):
        tracker.append(i1)

    while tracker[m-1]!=lenS:
        temp_value=0
        for index in tracker:
            temp_value+=s[index]
        if temp_value==d:
            to_return+=1
        
        tracker[0]+=1

        i=0
        while i<len(tracker)-1:
            if tracker[i]+1>lenS:
                tracker[i]=0
                tracker[i+1]+=1
            i+=1

    return to_return

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    #print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
