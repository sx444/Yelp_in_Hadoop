# question 3: get the average stars for each category in the interested area

# question 3 mapper

# latitude of 40.3577778 ~ 40.5244444 
# longitude of -79.8594444 ~ -80.0261111 

#!/usr/bin/env python

import sys
import json

categories = None
starsCount = None

for line in sys.stdin:
	data = json.loads(line.strip())
	if data['longitude'] <= -79.8594444\
		and data['longitude'] >= -80.0261111\
		and data['latitude'] >= 40.3577778\
		and data['latitude'] <= 40.5244444:
		for i in range(len(data['categories'])):
			categories = data['categories'][i].encode("utf-8")			
			starsCount = data['stars']
			print '%s^%s^%s' % (categories, starsCount, 1)