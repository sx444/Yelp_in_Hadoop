# !/usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip()
	userId,categories,stars = line.split('\t')
	print '%s^%s^%s^%s' % (userId,categories,stars,1)