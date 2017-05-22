# question 4: Rank reviewers by number of reviews. 
# For the top 10 reviewers, show their average number of stars, by category.

# mapper

#!/usr/bin/env python

import sys
import json

userId = None
reviewId = None

for line in sys.stdin:
	data = json.loads(line.strip())
	userId = data['user_id']
	reviewId = data['review_id']
	print '%s^%s^%s' % (userId, reviewId,1)


