Senti
---------

Senti is a Sentiment Analyzer based on AFINN.

Usage:
------

An example of how to get print the sentiment strength based on input text.

    	from senti_analysis import *

    	sample_sentence = "I like her."
    	print("%6.2f %s" % (sentiment(sample_sentence),sample_sentence))

If it prints a positive value, then it is a positive statement else a negative one.
If it prints zero value, it can be considered as Neutral.


