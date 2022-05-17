import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    count = 0
    pos_count = 0
    neg_count = 0
    zero_count = 0
    for item in arr:
        count += 1
        if item > 0:
            pos_count += 1
        elif item < 0:
            neg_count += 1
        else:
            zero_count += 1

    print(f"{pos_count/count:.6f}\n{neg_count/count:.6f}\n{zero_count/count:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
