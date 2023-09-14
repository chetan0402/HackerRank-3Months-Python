#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    tracker={}
    lowest_id=[]
    for ele in arr:
        try:
            tracker[ele]+=1
        except:
            tracker[ele]=1

    temp=0
    for key in tracker.keys():
        if tracker[key]>temp:
            temp=tracker[key]
            lowest_id=[key]
        if tracker[key]==temp:
            lowest_id.append(key)

    return sorted(lowest_id)[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
