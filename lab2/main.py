#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    matches = re.split("#k", format_string)
    if(len(matches) > 1):
        print(matches[0].swapcase() + param.swapcase() + matches[2].swapcase())
    
    matches = re.split("#.(\d*)k", format_string)
    if(len(matches) > 1):
        if int(matches[1]) != '':
            print(matches[0].swapcase() + param[:int(matches[1])].swapcase() + matches[2].swapcase())
    else:
        print(matches[0].swapcase())

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
