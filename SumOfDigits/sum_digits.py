import sys

with open(sys.argv[1]) as test_cases:
    for test in test_cases:
        numbers = [int(x) for x in test[:-1]]
        print str(sum(numbers))
