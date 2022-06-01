#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    triangles = []
    try:
        for i in range(len(sticks)):
            for j in range(i+1, len(sticks)):
                for k in range(j+1, len(sticks)):
                    if sticks[i]+sticks[j] > sticks[k]:
                        # print(list(sticks[i],sticks[j],sticks[k]))
                        triangles.append((sticks[i], sticks[j], sticks[k]))
    except:
        pass
    if len(triangles) == 0:
        return [-1]

    unique_triangles = list(set(triangles))
    print(triangles)
    print(unique_triangles)

    trianglePerimeter = {}
    for item in unique_triangles:
        trianglePerimeter[item] = sum(item)
    sortedPerimeter = {k: v for k, v in sorted(
        trianglePerimeter.items(), key=lambda item: item[1], reverse=True)}
    return next(iter(sortedPerimeter.keys()))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
