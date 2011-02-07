#!/usr/bin/python
# Week4 Assignment Subprocess "jsonout.py"

import sys, time, urlparse, json

class Jsonout(object):
	"""does some computation and return string in json format
	"""

	def __init__(self, argv):
		self.qdict = urlparse.parse_qs(argv[1])		# convert & store query string[dictionary]
		self.s_n1 = self.qdict.get('a')[0]			# store the value string of "a"
		self.s_n2 = self.qdict.get('b')[0]			# store the value string of "b"

	def __repr__(self):
		dct = {}
		n = int(self.s_n1) + int(self.s_n2)			# calucurate "num1 + num2"
		t = time.time()							# current time in float

		dct['result'] = n
		dct['uwnetid'] = 'hesumi'
		dct['time'] = t
		
		return json.dumps(dct, sort_keys = True, indent=4)			# return JSON format string


if __name__ == '__main__':
	jo = Jsonout(sys.argv)
	print jo
