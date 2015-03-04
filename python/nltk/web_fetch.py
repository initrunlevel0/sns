from __future__ import division
import nltk, re, pprint
from urllib import urlopen

# Open BBC news from Internet
# News: Blonde to die out in 200 years
html  = urlopen("http://news.bbc.co.uk/2/hi/health/2284783.stm").read()

raw = nltk.clean_html(html)

# Word tokenization
tokens = nltk.word_tokenize(raw)




