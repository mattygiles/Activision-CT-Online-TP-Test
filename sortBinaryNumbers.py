#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'sortBinaryNumbers' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY bitArrays as parameter.


def sortBinaryNumbers(bitArrays):
    array = [[0, i] for i in range(len(bitArrays))]

    for i in range(len(bitArrays)):
        for bit in bitArrays[i]:
            array[i][0] = array[i][0] | (1 << bit)

    array.sort(reverse=True)
    return [element[1] for element in array]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bitArrays_rows = int(input().strip())
    bitArrays_columns = int(input().strip())

    bitArrays = []

    for _ in range(bitArrays_rows):
        bitArrays.append(list(map(int, input().rstrip().split())))

    result = sortBinaryNumbers(bitArrays)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
