#!/usr/bin/python

import time
import re
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# Replace USERNAME with your twitter username
url = u'http://twitter.com/psibi?page=%s'
tweets_file = open('tweets', 'w')
for x in range(10*10000):
    f = urlopen(url % x)
    soup = BeautifulSoup(f.read())
    f.close()
    tweets = soup.findAll('span', {'class': 'entry-content'})
    if len(tweets) == 0:
        break
    [tweets_file.write(x.renderContents() + '\n') for x in tweets]
    # being nice to twitter's servers
    time.sleep(2)

tweets_file.close()





    
