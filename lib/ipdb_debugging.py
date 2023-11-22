#!/usr/bin/env python3

import ipdb
def plus_two(x):
    num = x + 2
    if num > 0:
        ipdb.set_trace()
    return num

