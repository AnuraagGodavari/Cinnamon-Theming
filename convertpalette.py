#!/usr/bin/python3

import re, sys, pprint, json
from getcolors import *
from convertcolors import *

def convertpalette(infile, outfile = None, mode = None):
	
	palette = dict()
	css_tochange = None	
	oldcss = None

	with open(infile) as f:
		palette = json.load(f)

	oldcolors = getcolors(outfile)

	#If palette is in rgb mode, map hex colors to values
	if (mode in ("rgb", "rgba")):
		palette = {color: palette[hex_to_rgb(color)] for color in oldcolors if hex_to_rgb(color) in palette.keys()}
	
	with open(outfile) as f:
		oldcss = f.read()
	
	for color in palette.keys():
		print(f"\"{color}\", {palette[color]}")
		oldcss = oldcss.replace(color, palette[color])

	with open(outfile, 'w') as f:
		f.write(oldcss)

	#pprint.pprint(list(palette))

def main():

	infile = sys.argv[1]

	outfile = None
	mode = None

	if (len(sys.argv) > 2):
		outfile = sys.argv[2]

	if (len(sys.argv) > 3):
		mode = sys.argv[3]

	convertpalette(infile, outfile, mode)

if __name__ == '__main__':
	if (len(sys.argv) <= 1):
		raise Exception("Too few arguments")

	main()
