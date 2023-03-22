#!/usr/bin/python3

import re, sys

def getcolors(file):
	
	css = ""

	with open(file) as f:
		css = f.read()

	print(set([''.join(patterns) for patterns in re.findall("(rgba?\(.*\))|(#[1234567890abcdeABCDE]{6})", css)]))

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		raise Exception("Too few arguments")

	getcolors(sys.argv[1])	
