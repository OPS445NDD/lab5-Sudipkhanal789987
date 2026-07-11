#!/usr/bin/env python3

# Author: Sudip Khanal
# Author ID: skhanal15
# Date Created: 2026/05/17

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
