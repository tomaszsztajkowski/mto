#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    matches = re.split("#.(\d*)g", format_string)
    if(len(matches) > 1):
        if int(matches[1]) != '':
            param = "".join([str((int(d)*9+1)%10) for d in param])
            new_format = matches[0] + "%" + matches[1] + "d" + matches[2]
            sys.stdout.write(new_format % int(param))
        return
    else:
        print(matches[0])

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
    