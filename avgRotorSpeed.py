#!/bin/python3

import math
import os
import random
import re
import sys

import requests
import json


#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId


def avgRotorSpeed(statusQuery, parentId):
    result = requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?status=' + statusQuery).json()
    pages = result['total_pages']
    count = 0
    total = 0

    for page in range(1, pages + 1):
        request = requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?status=' + statusQuery + '&page=' + str(page)).json()
        data = request['data']

        for i in range(10):
            try:
                id = data[i]['parent']['id']
                # print('parentId = ' + str(id))

                if id == parentId:
                    rotorSpeed = data[i]['operatingParams']['rotorSpeed']
                    # print('rotorSpeed = ' + str(rotorSpeed))
                    total = total + rotorSpeed
                    count = count + 1
            except:
                pass

    if total == 0 or count == 0:
        return 0
    else:
        output = int(total / count)
        return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    parentId = int(input().strip())

    result = avgRotorSpeed(statusQuery, parentId)

    fptr.write(str(result) + '\n')

    fptr.close()
