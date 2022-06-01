#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    cnt = Counter(arr)
    sorted_arr = cnt.most_common()
    max_count = sorted_arr[0][1]
    max_birds = []
    for item in sorted_arr:
        if item[1] == max_count:
            max_birds.append(item[0])
    max_birds.sort()
    return max_birds[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
