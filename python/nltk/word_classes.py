from __future__ import division
import nltk, re, pprint
from urllib import urlopen

# WORD CLASSES
# Belajar mengklasifikasikan kata (kata benda, kata sifat, dkk)

# POS Tagging
# Merupakan mekanisme untuk menandai (tag) kata dengan suatu kelas tertentu pada proses NLP
# Menjadi suatu kelas kata atau kategori leksikal

# Tagger
text = nltk.word_tokenize("And now for something completely different")
tags = nltk.pos_tag(text)
print tags
print "#######"

# Info utama :
# Tagging pada NLTK: Menggunakan tupple dua item
# ('fly', 'NN')

# [('And', 'CC'), ('now', 'RB'), ('for', 'IN'), ('something', 'NN'), ('completely', 'RB'), ('different', 'JJ')]

# Keterangan hasil
# * CC: Coordinating Conjunction
# * RB: Adverbs
# * IN: Preposition
# * NN: Noun
# * JJ: Adjective

# Dalam bahasa inggris, kadang ada satu kata yang sama penulisannya (walaupun homofon atau tidak), tapi memiliki kelas yang berbeda

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
tags = nltk.pos_tag(text);
print tags
print "#######"

# [('They', 'PRP'), ('refuse', 'VBP'), ('to', 'TO'), ('permit', 'VB'), ('us', 'PRP'), ('to', 'TO'), ('obtain', 'VB'), ('the', 'DT'), ('refuse', 'NN'), ('permit', 'NN')]


# Apa kegunaan dari klasifikasi ini, lihat contoh berikut
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print text.similar('woman')

# Hasil :
# bman day time year car moment world family house boy child country job
# state girl place war way case question

# Dari kata woman (Noun/Kata Benda) tadi, kita bisa mencari kata yang mirip penggunaannya dengan woman (N) ini.
# Seperti pada hasil di atas.

# Belajar kembali kelas kata

# NOUNS: Refer ke orang, tempat, sesuatu, dll. Ditempatkan setelah penentu atau kata sifat
# VERB: Refer to event atau action. Menyatakan hubungan antara dua frasa NOUN
# ADJECTIVE: Describe verb
# ADVERB: Modify verb (timing, manner, place)



