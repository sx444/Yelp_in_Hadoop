# q1 summarize number of reviews by US city, by business category
# input is just business file


#!/usr/bin/env python

import sys
import json

UScityName = None
reviewCount = None
categories = None

for line in sys.stdin:

	data = json.loads(line.strip())
	if data['city'] == 'Pittsburgh'\
		or data['city'] == 'Charlotte'\
		or data['city'] == 'Champaign'\
		or data['city'] == 'Phoenix'\
		or data['city'] == 'Las Vegas'\
		or data['city'] == 'Madison': 
		for i in range(len(data['categories'])):
			UScityName = data['city'].encode("utf-8")
			categories = data['categories'][i].encode("utf-8")
			reviewCount = data['review_count']
			print '%s^%s^%s' % (UScityName, categories, reviewCount)



