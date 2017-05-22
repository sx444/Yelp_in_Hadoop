# !/usr/bin/env python

import sys
import json
from operator import itemgetter

current_UScityName = None
current_categories = None
current_reviewCount = 0

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	UScityName, categories, reviewCount = line.split('^')
	
	try:
		reviewCount = int(reviewCount)
	except ValueError:
		continue
		
	# works because Hadoop sorts map output
	if current_UScityName == UScityName and current_categories == categories:
		current_reviewCount += reviewCount
	else:
		if current_UScityName and current_categories:
			print '%s\t%s\t%s' % (current_UScityName, current_categories, current_reviewCount)
		current_reviewCount = reviewCount
		current_categories = categories
		current_UScityName = UScityName
