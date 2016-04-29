import sys

def returnSingleChars(string):
    single_chars = []
    for char in string:
        if single_chars.count(char) > 0:
            single_chars.remove(char)
        else:
            single_chars.append(char)
    return single_chars

with open(sys.argv[1]) as test_cases:
    for test in test_cases:
        print returnSingleChars(test[:-1])[0]
