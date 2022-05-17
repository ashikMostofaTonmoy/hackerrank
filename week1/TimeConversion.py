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

    time_string = s.split(":")

    if time_string[2][2] == 'A' and int(time_string[0]) == 12:
        return f"{'00'}:{time_string[1]}:{time_string[2][:2]}"

    elif time_string[2][2] == 'A' and int(time_string[0]) != 12:
        return f"{time_string[0]}:{time_string[1]}:{time_string[2][:2]}"

    elif time_string[2][2] == 'P' and int(time_string[0]) != 12:
        return f"{int(time_string[0]) + 12}:{time_string[1]}:{time_string[2][:2]}"

    elif time_string[2][2] == 'P' and int(time_string[0]) == 12:
        return f"{time_string[0]}:{time_string[1]}:{time_string[2][:2]}"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
