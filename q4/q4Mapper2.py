#!/usr/bin/env python

import sys
import json

for line in sys.stdin:

	categories = "-1"
	businessId = "-1"
	userId = "-1"
	stars = "-1"
       
	data = json.loads(line.strip())
	if len(data) == 8: # review data
		if data['user_id'] == 'kGgAARL2UmvCcTRfiscjug'\
			or data['user_id'] == 'Iu3Jo9ROp2IWC9FwtWOaUQ'\
			or data['user_id'] == '9A2-wSoBUxlMd3LwmlGrrQ'\
			or data['user_id'] == 'DrWLhrK8WMZf7Jb-Oqc7ww'\
			or data['user_id'] == 'glRXVWWD6x1EZKfjJawTOg'\
			or data['user_id'] == 'ia1nTRAQEaFWv0cwADeK7g'\
			or data['user_id'] == '3gIfcQq5KxAegwCPXc83cQ'\
			or data['user_id'] == 'uZbTb-u-GVjTa2gtQfry5g'\
			or data['user_id'] == 'fczQCSmaWF78toLEmb0Zsw'\
			or data['user_id'] == '5lq4LkrviYgQ4LJNsBYHcA':
			
			userId = data['user_id'].encode("utf-8")
			businessId = data['business_id'].encode("utf-8")
			stars = data['stars']
			print '%s^%s^%s^%s' % (businessId,stars,userId,categories)	
		
	if len(data) == 15: # business data
		for i in range(len(data['categories'])):
			businessId = data['business_id'].encode("utf-8")
			categories = data['categories'][i].encode("utf-8")
			print '%s^%s^%s^%s' % (businessId,stars,userId,categories)
		    
		