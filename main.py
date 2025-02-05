#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year < 1700 or year > 2700:
        print ()
            
    elif year==1918:
        print ('26.09.1918')

    elif year < 1918:
        if year%4==0:
            print(f"12.09.{year}")
                    
        else:
            print(f"13.09.{year}")
                
    elif year > 1918:
        if year%400==0 or year%4==0 and year%100!=0:
            print(f"12.09.{year}") 

        else:
            print(f"13.09.{year}")
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    # fptr.write(result + '\n')

    # fptr.close()
