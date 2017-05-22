#!/usr/bin/env python

import sys
import json

businessName = None
businessId = None
stars = None

# input is the file of business and review
for line in sys.stdin:
	data = json.loads(line.strip())
	if data['longitude'] <= -79.8594444 and data['longitude'] >= -80.0261111 and data['latitude'] >= 40.3577778 and data['latitude'] <= 40.5244444:
		for i in range(len(data['categories'])):
			if data['categories'][i] == 'Food':
				businessName = data['name'].encode("utf-8")			
				businessId = data['business_id'].encode("utf-8")						
				stars = data['stars']
				print '%s\t%s\t%s' % (stars,businessName,businessId)