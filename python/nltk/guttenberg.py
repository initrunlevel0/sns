from __future__ import division
import nltk, re, pprint

# Open Gutenberg
text = open("2554.txt", "r").read()

# Tokenize

tokens = nltk.word_tokenize(text)
print tokens[:10]
