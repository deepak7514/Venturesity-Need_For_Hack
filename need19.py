#!/usr/bin/python
"""
" Input : String
" Output: Count of vowels including 'y'

" USAGE
" python need19.py --input 'string'
" python need19.py
"""
# import the necessary packages
import string
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help="input string")
args = vars(ap.parse_args())

# User Input
if not args.get("input", False):
    inp=raw_input('Enter string: ').strip()
else:
    inp=args["input"]

# Considering both uppercase and lowercase characters
inp=inp.lower()
while True:
    if inp=='':
        print 'Input string cannot be empty'
    elif set(inp).intersection(string.digits):
        print 'Input string cannot contain any numbers'
    else:
        break
    inp=raw_input('Enter string: ').strip().lower()

# vowels considering 'y' as a vowel
vowels=['a','e','i','o','u']+['y']
# counter for counting vowels
cnt=0
for i in vowels:
    # S.count(sub[, start[, end]]) -> int
    # Return the number of non-overlapping occurrences of
    # substring sub in string S[start:end].
    cnt+=inp.count(i)

# Output
print 'Output: %d'%cnt
