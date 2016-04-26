import sys
import string

_BASE_ = len(string.ascii_letters)

def ExcelBase(num):
    length = 0
    converted = ''
    while num > 0:
        converted[length] = num % _BASE_
        num /= _BASE_
        length += 1
