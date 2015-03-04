from __future__ import division
import nltk, re, pprint
from urllib import urlopen

# SEGMENTATION
# Sentence Segmentation: Memecah kalimat
# Pada corpus bawaan, pemecahaan sudah dilakukan dengan rapi. Contoh

print nltk.corpus.brown.words()
print nltk.corpus.brown.sents()
print "#######"

# Untuk teks lainnya, salah satu teknik segementasi kalimat bisa menggunakan punkt

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[171:181])
print "#######"

# Kenapa tidak pisah saja berdasarkan tanda titik? Kadang tanda titik tidak hanya digunakan untuk pemisah kalimat saja




