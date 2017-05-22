# 2. Rank the US cities by # of stars for each category
# rank the US cities based on the number of stars for each category

# mapper

#!/usr/bin/env python

import sys
import json

categories = None
UScityName = None
starsCount = None

for line in sys.stdin:
	data = json.loads(line.strip())
	if data['city'] == 'Pittsburgh' or data['city'] == 'Charlotte' or data['city'] == 'Champaign' or data['city'] == 'Phoenix' or data['city'] == 'Las Vegas' or data['city'] == 'Madison': 
		for i in range(len(data['categories'])):
			categories = data['categories'][i].encode("utf-8")
			UScityName = data['city'].encode("utf-8")
			starsCount = data['stars']
			print '%s^%s^%s' % (categories, UScityName, starsCount)

