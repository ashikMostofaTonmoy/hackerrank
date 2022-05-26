#
# alphabet_string = string.ascii_lowercase
# # Create a string of all lowercase letters
# alphabet_string = string.ascii_uppercase

# alphabet_list = list(alphabet_string)
# # Create a list of all lowercase letters


# print(alphabet_list)


#!/bin/python3

from collections import OrderedDict, Counter
import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    # Write your code here
    alphabet = string.ascii_lowercase
    alphabet_list = list(alphabet)

    od = OrderedDict()
    for letter in alphabet_list:
        od[letter] = 0

    c = Counter(s.lower())

    for key, value in c.items():
        od[key] = value

    if 0 in list(od.values()):
        return f"not pangram"
    else:
        return f"pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
