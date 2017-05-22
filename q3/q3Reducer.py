# q3 reducer

# !/usr/bin/env python

import sys
import json
from operator import itemgetter

current_categories = None
current_starsCount = 0
current_businessCount = 0

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	categories, starsCount, businessCount = line.split('^')
	
	try:
		starsCount = float(starsCount)
		businessCount = int(businessCount)
	except ValueError:
		continue
		
	# works because Hadoop sorts map output
	if current_categories == categories:
		current_starsCount += starsCount
		current_businessCount += 1
		
	else:
		if current_categories:
			print '%s\t%s\t%s' % (current_categories, current_starsCount, current_businessCount)
		current_categories = categories
		current_starsCount = starsCount
		current_businessCount = 1