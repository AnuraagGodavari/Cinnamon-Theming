#!/usr/bin/python3

import re, sys, pprint, json

def rgb_to_hex(color):
	pass

def hex_to_rgb(color):
	pass

def getcolors(infile, outfile = None, mode = None):
	
	css = ""

	with open(infile) as f:
		css = f.read()

	palette = {color: "" for color in set([''.join(patterns) for patterns in re.findall("(rgba?\(.*\))|(#[1234567890abcdeABCDE]{6})", css)])}

	if outfile:
		with open(outfile, 'w') as f:
			json.dump(palette, f, indent = 4)

	#pprint.pprint(list(palette))

def main():

	infile = sys.argv[1]

	outfile = None
	if (len(sys.argv) > 2):
		outfile = sys.argv[2]

	getcolors(infile, outfile)

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		raise Exception("Too few arguments")

	main()
