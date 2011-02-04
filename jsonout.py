#!/usr/bin/python
# Week4 Assignment Subprocess "jsonout.py"

import sys, time

class Jsonout(object):
	"""does some computation and return string in json format
	"""

	def __init__(self, argv):
		self.s_n1 = argv[1]		# store number1 to local variable
		self.s_n2 = argv[2]		# store number2 to local variable

	def __repr__(self):
		ADD_NUMS =\
		"""<html>
<head><title>Add Result</title></head>
<body>
<pre>
{
	"result": %s,
	"uwnetid": "hesumi",
	"time": %s
}
</pre>
</body>
</html>"""

		s_n = str(int(self.s_n1) + int(self.s_n2))	# calucurate "num1 + num2"
		s_time = str(time.time())					# current time in float
		return ADD_NUMS % (s_n, s_time)				# return JSON format string


if __name__ == '__main__':
	jo = Jsonout(sys.argv)
	print jo
