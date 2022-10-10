#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sortBinaryNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY bitArrays as parameter.
#


def compare(index1, index2, bitArrays):
    for i in range(len(bitArrays[index1])):
        if (bitArrays[index1][i] > bitArrays[index2][i]):
            return 1
        elif (bitArrays[index1][i] < bitArrays[index2][i]):
            return -1
    return 0
            

def compare_to_keys(my_compares, bitArrays):
    class A:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return my_compares(self.obj, other.obj, bitArrays) < 0
        def __gt__(self, other):
            return my_compares(self.obj, other.obj, bitArrays) > 0
        def __eq__(self, other):
            return my_compares(self.obj, other.obj, bitArrays) == 0
        def __le__(self, other):
            return my_compares(self.obj, other.obj, bitArrays) <= 0
        def __ge__(self, other):
            return my_compares(self.obj, other.obj, bitArrays) >= 0
        def __ne__(self, other):
            return my_compares(self.obj, other.obj, bitArrays) != 0
    return A

    
def sortBinaryNumbers(bitArrays):
    for value in bitArrays:
        value.sort(reverse = True)
        
    array = [i for i in range(len(bitArrays))]
    array.sort(reverse = True, key=compare_to_keys(compare, bitArrays))
    return array


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
