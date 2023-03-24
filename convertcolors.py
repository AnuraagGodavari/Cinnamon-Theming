#!/usr/bin/python3

import re

def rgb_to_hex(color):
	return color

def hex_to_rgb(color):
	
	if (re.search("#[1234567890abcdefABCDEF]{6}", color)):
		return f"rgb({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:], 16)})"

	return color

