#!/usr/bin/env python
from __future__ import print_function, division

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

line1 = eval(sys.stdin.readline())

print("upper-level keys")
pp.pprint(line1.keys())

print('')
print('user')
pp.pprint(line1['user'])

print('')
print('screen_name')
pp.pprint(line1['user']['screen_name'])
