#!/usr/bin/python3

import re, sys, pprint, json
from getcolors import *

def main():

	superpalette = dict()

	for filename in sys.argv[2:]:
		superpalette = superpalette | getcolors(filename, None, 'rgb')

	with open(sys.argv[1], 'w') as f:
		json.dump(superpalette, f, indent = 4)

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		raise Exception("Too few arguments")

	main()
