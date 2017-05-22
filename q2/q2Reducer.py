# q2 reducer

# !/usr/bin/env python

import sys
import json
from operator import itemgetter

current_categories = None
current_UScityName = None
current_starsCount = 0
current_businessCount = 0

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	categories, UScityName, starsCount = line.split('^')
	
	try:
		starsCount = float(starsCount)
	except ValueError:
		continue
		
	# works because Hadoop sorts map output
	if current_UScityName == UScityName and current_categories == categories:
		current_starsCount += starsCount
		current_businessCount += 1
		
	else:
		if current_UScityName and current_categories:
			print '%s\t%s\t%s\t%s' % (current_categories, current_UScityName, current_starsCount, current_businessCount)
		current_categories = categories
		current_UScityName = UScityName
		current_starsCount = starsCount
		current_businessCount = 1