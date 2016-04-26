import sys
import re

with open(sys.argv[1], 'r') as test_cases:
    val = 0
    for test in test_cases:
        val += int(test)
    print val
