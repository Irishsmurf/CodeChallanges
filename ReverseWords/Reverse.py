import sys

def reverse(words):
    words.reverse()
    print ' '.join(words)

with open(sys.argv[1]) as test_cases:
    for test in test_cases:
        test = test[:-1]
        wordlist = test.split(' ')
        reverse(wordlist)
