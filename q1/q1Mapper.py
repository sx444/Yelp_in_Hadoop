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




''' 
import sys
import json
 
# input comes from STDIN (standard input)
for line in sys.stdin:

    reviewCount = "-1"
    businessType = "-1" #default sorted as first
    UScityName = "-1" #default sorted as first
    businessName = "-1" #default sorted as first
 
    data = json.loads(line.strip())
    	  	 
    if data['city'] == 'Pittsburgh' or data['city'] == 'Charlotte' or data['city'] == 'Urbana-Champaign' or data['city'] == 'Phoenix' or data['city'] == 'Las Vegas' or data['city'] == 'Madison': # business data
        UScityName = data['city'].encode("utf-8")
        reviewCount = data['review_count']
        businessType = data['type'].encode("utf-8")
        businessName = data['name'].encode("utf-8")
        
    print '%s^%s^%s^%s' % (UScityName,businessType,businessName,reviewCount)
'''