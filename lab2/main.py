#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    matches = re.split("\#(\d*)k", format_string)
    if(len(matches) > 1):
        print(matches[0] + param[:int(matches[1])] + matches[2])
    else:
        print(matches[0])

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
