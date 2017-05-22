#!/usr/bin/env python


import sys
import json
from datetime import datetime

businessId = None
monthName = None
stars = None

# the input is the file of review
for line in sys.stdin:
	data = json.loads(line.strip())
	if len(data) == 8: # review data
		if data['business_id'] == 'EpPfFCLETEnzAw324Y666A'\
			or data['business_id'] == 'acvpqVAsH8steBaqjCCBaQ'\
			or data['business_id'] == 'BqsS2Y_-E2lUWS-f2jYadw'\
			or data['business_id'] == 'AvVMhXghvAE2_JGWXoC7IA'\
			or data['business_id'] == 'kHLZZxEhqykXMED30oqgUw'\
			or data['business_id'] == '6BE16zjI11ie57QFCat-Jg'\
			or data['business_id'] == 'aqslMehKRH-jsS9lUlmZeg'\
			or data['business_id'] == 'xJ-Vq01ULNg_9-4CovAUbw'\
			or data['business_id'] == '08eRFhpedodAf6atSRK09g'\
			or data['business_id'] == '7B7ncPm1BLWDhvWFdPdVAA'\
			or data['business_id'] == 'wSss_Alw88phYPdtAPs-lA'\
			or data['business_id'] == 'gNcvmWQ6b40mpfzSOdStEA'\
			or data['business_id'] == '9KsHPdF1-P_CiXnvugdQvQ'\
			or data['business_id'] == 'cZl7-Um4HiJWFgDVmMan2Q'\
			or data['business_id'] == '6C1Igw4BzRmg5Et8GSVfpA'\
			or data['business_id'] == 'DMCNGlV2VA6dkD6z22bohw'\
			or data['business_id'] == '9q0T11qr73CgUlLM1amWMA'\
			or data['business_id'] == 'ionFxm0fkwX_J3I5By6Efg'\
			or data['business_id'] == 'XmJJQjudjE7bXZyFsH0ECw'\
			or data['business_id'] == 'EZdFJ0Uxqarqs5BX3pKgug': 
				businessId = data['business_id'].encode("utf-8")	
				monthName = datetime.strptime(data['date'], "%Y-%m-%d").strftime('%B')
				stars = data['stars']
				print '%s^%s^%s' % (businessId, monthName, stars)
	 