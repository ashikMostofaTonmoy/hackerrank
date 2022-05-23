#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    od = OrderedDict()
    for i in range(100):
        od[i] = 0

    # print(od)

    c = dict(Counter(arr))

    for key, value in c.items():
        od[key] = value

    return list(od.values())
    # return list()
    # dict(od)
    # print(list(dict(od).values))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
