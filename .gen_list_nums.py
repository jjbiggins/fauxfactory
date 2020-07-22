import sys
import os
import fauxfactory

def gen_list_nums(minVal, maxVal, listSize):
    rand_nums = []
    
    while (range(listSize)):
        rand_num = fauxfactory.gen_number(minVal, maxVal, 10)
        rand_nums.append(rand_num)
        listSize = listSize - 1

    return rand_nums
