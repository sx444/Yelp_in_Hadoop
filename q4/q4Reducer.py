# q4 reducer

# !/usr/bin/env python

			
	
import sys
import json
from operator import itemgetter


current_userId = None
current_reviewId = None
current_reviewsCount = 0

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	userId, reviewId,reviewsCount = line.split('^')
	
	try:
		reviewsCount = int(reviewsCount)
	except ValueError:
		continue
				
	# works because Hadoop sorts map output
	if current_userId == userId:
		current_reviewsCount += 1
		
	else:
		if current_userId:
			print '%s\t%s' % (current_userId,current_reviewsCount)
		current_userId = userId
		current_reviewId = reviewId
		current_reviewsCount = 1
