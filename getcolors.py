#!/usr/bin/python3

import re, sys, pprint, json
from convertcolors import *

def getcolors(infile, outfile = None, mode = None):
	
	css = ""

	convert_func = None
	if mode == "hex":
		convert_func = rgb_to_hex
	elif mode in ("rgb", "rgba"):
		convert_func = hex_to_rgb

	with open(infile) as f:
		css = f.read()

	patterns = set([''.join(matches) for matches in re.findall("(rgba?\(.*\))|(#[1234567890abcdefABCDEF]{6})", css)])
	
	if (convert_func): patterns = [convert_func(color) for color in patterns]

	palette = {color: color for color in patterns}

	if outfile:
		with open(outfile, 'w') as f:
			json.dump(palette, f, indent = 4)
	
	return palette

	#pprint.pprint(list(palette))

def main():

	infile = sys.argv[1]

	outfile = None
	mode = None

	if (len(sys.argv) > 2):
		outfile = sys.argv[2]

	if (len(sys.argv) > 3):
		mode = sys.argv[3]

	getcolors(infile, outfile, mode)

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		raise Exception("Too few arguments")

	main()
