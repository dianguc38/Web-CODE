#!/usr/bin/env python
from __future__ import print_function
import sys

message = raw_input('Enter message to encode:')

print('Decoded string (in ASCII):\n')
for ch in message:
   print('.concat(T(java.lang.Character).toString(%s))' % ord(ch), end=""), 
print('\n')
