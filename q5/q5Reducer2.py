# !/usr/bin/env python

import sys
import json
from operator import itemgetter
from datetime import datetime

current_businessId = None
current_monthName = None
current_stars = 0
current_reviewCount = 0


# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	businessId, monthName, stars = line.split('^')
	
	try:
		stars = float(stars)
	except ValueError:
		continue
		
	if current_businessId == businessId and current_monthName == monthName:
		current_stars += stars
		current_reviewCount += 1
		
	else:
		if current_businessId and current_monthName:
			print '%s\t%s\t%s\t%s\t%s' % (current_businessId, current_monthName, current_stars, current_reviewCount, current_stars/current_reviewCount)
		current_businessId = businessId
		current_monthName = monthName
		current_stars = stars
		current_reviewCount = 1		
		