#!/usr/bin/env python
  
import sys

current_userId = None
current_categories = None
current_stars = 0
current_count = 0

for line in sys.stdin:
	userId,categories,stars,count = line.split('^')
	
	try:
		count = int(count)
		stars = float(stars)
	except ValueError:
		continue

	if current_categories == categories and current_userId == userId:
		current_count += count
		current_stars += stars
	else:
		if current_categories and current_userId:
			print '%s\t%s\t%s' % (current_userId, current_categories, current_stars/current_count)
		current_count = count
		current_userId = userId
		current_categories = categories
		current_stars = stars