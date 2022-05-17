#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    count_score = [0, 0]

    for value in scores:
        if max_score < value:
            count_score[0] += 1
            max_score = value
        elif min_score > value:
            count_score[1] += 1
            min_score = value
        else:
            pass

    return count_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
