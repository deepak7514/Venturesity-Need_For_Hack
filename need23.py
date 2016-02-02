# USAGE
# python need23.py --input integer

# import the necessary packages
import argparse
from math import factorial

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input",
	help = "Input Integer (Range 0 to 1000)")
args = vars(ap.parse_args())

if args['input']:
    inp=args['input']
else:
    inp = raw_input("Input Integer = ")
if not inp.isdigit():
    print 'Input Integer should be a number (0 to 1000)'
else:
    inp = int(inp)
    if inp<0 or inp>1000:
        print 'Input Integer should be less than 1000'
    else:
        print 'Factorial = %d'%factorial(inp)
