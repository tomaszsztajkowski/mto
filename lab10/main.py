#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    matches = re.split("#a", format_string)
    if(len(matches) > 1):
        param = int(param) // len(str(int(param)))
        if param % 2 == 0:
            sys.stdout.write(format_string.replace('#a', '%d') % int(param))
        else:
            sys.stdout.write(format_string.replace('#a', '%x') % int(param))
        print()
        return
    else:
        print(matches[0])

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
    