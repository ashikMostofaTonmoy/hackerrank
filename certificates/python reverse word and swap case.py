#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    # print(sentence)
    splited_string = sentence.split(' ')
    splited_string.reverse()
    new_string = ' '.join(map(str, splited_string))
    csechanged = ''

    for i in range(len(new_string)):
        if new_string[i].islower() == True:
            # print(new_string[i])
            csechanged += new_string[i].upper()
            # print(new_string[i])
        else:
            # print(new_string[i])
            csechanged += new_string[i].lower()
            # print(new_string[i])
    # print(csechanged)
    return csechanged


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
