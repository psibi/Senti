#!/usr/bin/python

import re

class ctweet:

    def clean_tweets(self):
        fhandler = open('tweets','r')
        text = fhandler.read()
        fhandler.close()
        ctext = self._clean_file(text)
        fhandler = open('ctweets','w')
        fhandler.write(ctext)
        fhandler.close()
        
    def _clean_file(self,text):
        return  re.sub(r'<[^>]*?>', '', text)

if __name__=="__main__":
    ctwt = ctweet()
    ctwt.clean_tweets()
