#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    converted = ''
    for i, digit in enumerate(bin(int(param))[::-1][:-2]):
        converted = converted + ('0' if digit == '0' else chr(i % 26 + 97))
    
    print(format_string.replace('#b', converted[::-1]))


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
    