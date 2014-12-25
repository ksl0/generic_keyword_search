#from django.conf import settings

import twit

total = twit.twitter.search(q='cheesestick', count=2)

text = []
username = []
text = total['statuses'][0]['text']
username = total['statuses'][0]['user']['screen_name']



