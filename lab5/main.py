#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    # matches = re.split("#k", format_string)
    # if(len(matches) > 1):
    #     print(matches[0].swapcase() + param.swapcase() + matches[1].swapcase())
    #     return
    
    matches = re.split("#\.(\d*)g", format_string)
    if(len(matches) > 1):
        if int(matches[1]) != '':
            param = "".join([9 if d == '0' else int(d) - 1 for d in param])
            print(matches[0] + param[:int(matches[1])] + matches[2])
        return
    else:
        print(matches[0])

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
