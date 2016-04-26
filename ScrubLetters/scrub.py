import sys
import re

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        regex = ''
        explode = test.split(', ')
        for char in explode[1]:
            regex += char + '|'
        print re.sub('('+regex+')', '', explode[0])
