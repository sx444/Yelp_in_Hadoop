# !/usr/bin/env python

import sys
import json
from operator import itemgetter

current_categories = None
current_userId = None
current_businessId = None
current_stars = 0

for line in sys.stdin:
	line = line.strip()

	businessId,stars,userId,categories = line.split('^')
	if userId == "-1":
		current_businessId = businessId
		current_categories = categories
	else:
		if current_businessId == businessId:
			current_stars = stars
			current_userId = userId
			print '%s\t%s\t%s' % (current_userId,current_categories,current_stars)
    				


