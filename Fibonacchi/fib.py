import sys
import math

_PHI = (1+math.sqrt(5))/2
_MINUS_PHI = (1-math.sqrt(5))/2

def CalculateFib(pow):
    return int((math.pow(_PHI, pow) - math.pow(_MINUS_PHI, pow))/math.sqrt(5))

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print str(CalculateFib(int(test)))
