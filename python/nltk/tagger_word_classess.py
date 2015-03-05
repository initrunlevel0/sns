from __future__ import division
import nltk, re, pprint
from nltk.corpus import brown

# Belajar kembali kelas kata

# NOUNS: Refer ke orang, tempat, sesuatu, dll. Ditempatkan setelah penentu atau kata sifat
# VERB: Refer to event atau action. Menyatakan hubungan antara dua frasa NOUN
# ADJECTIVE: Describe verb
# ADVERB: Modify verb (timing, manner, place)

# TAGGER
# NLTK memiliki mekanisme untuk menandai "tagging" segmen kata.

# DefaultTagger
# Tag dengan penanda default yang sama

raw = "I do not like green eggs and ham, I do not like the Sam I am!"
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print default_tagger.tag(tokens)
print "###"

# [('I', 'NN'), ('do', 'NN'), ('not', 'NN'), ('like', 'NN'), ('green', 'NN'), ('eggs', 'NN'), ('and', 'NN'), ('ham', 'NN'), (',', 'NN'), ('I', 'NN'), ('do', 'NN'), ('not', 'NN'), ('like', 'NN'), ('the', 'NN'), ('Sam', 'NN'), ('I', 'NN'), ('am', 'NN'), ('!', 'NN')]

# RegexpTagger
# Menggunakan tagging berbasis regex

patterns = [
    (r'.*ing$', 'VBG'),  # gerund
    (r'.*ed$', 'VBD'),   # simple past
    (r'.*es$', 'VBZ'),   # 3rd singular present
    (r'.*ould$', 'MD'),   # modals
    (r'.*\'s$', 'NN$'),   # possessive noun
    (r'.*s$', 'NNS'),     # plural noun
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal number
    (r'.*', 'NN')         # noun (default)
]

regexp_tagger = nltk.RegexpTagger(patterns)
print regexp_tagger.tag(brown.sents(categories='news')[3])
print "###"

# [('``', 'NN'), ('Only', 'NN'), ('a', 'NN'), ('relative', 'NN'), ('handful', 'NN'), ('of', 'NN'), ('such', 'NN'), ('reports', 'NNS'), ('was', 'NNS'), ('received', 'VBD'), ("''", 'NN'), (',', 'NN'), ('the', 'NN'), ('jury', 'NN'), ('said', 'NN'), (',', 'NN'), ('``', 'NN'), ('considering', 'VBG'), ('the', 'NN'), ('widespread', 'NN'), ('interest', 'NN'), ('in', 'NN'), ('the', 'NN'), ('election', 'NN'), (',', 'NN'), ('the', 'NN'), ('number', 'NN'), ('of', 'NN'), ('voters', 'NNS'), ('and', 'NN'), ('the', 'NN'), ('size', 'NN'), ('of', 'NN'), ('this', 'NNS'), ('city', 'NN'), ("''", 'NN'), ('.', 'NN')



# LookupTagger / UnigramTagging
# Menggunakan tag berdasarkan statistik: tag mana yang paling condong ke suatu kata.

fd = nltk.FreqDist(brown.words(categories='news'))   # Format: {kata: distribusi}
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news')) # Format: Seperti tupple tagging

most_freq_words = fd.keys()[:100] # Ambil 100 kata terbanyak

likely_tags = dict((word, cfd[word].max()) for word in most_freq_words) # Untuk setiap kata, ambil yang jenisnya terbanyak
print likely_tags

baseline_tagger = nltk.UnigramTagger(model=likely_tags)

sent = brown.sents(categories='news')[3]
print baseline_tagger.tag(sent)
print "###"

#[('``', '``'), ('Only', None), ('a', 'AT'), ('relative', None), ('handful', None), ('of', 'IN'), ('such', None), ('reports', None), ('was', 'BEDZ'), ('received', None), ("''", "''"), (',', ','), ('the', 'AT'), ('jury', None), ('said', 'VBD'), (',', ','), ('``', '``'), ('considering', None), ('the', 'AT'), ('widespread', None), ('interest', None), ('in', 'IN'), ('the', 'AT'), ('election', None), (',', ','), ('the', 'AT'), ('number', None), ('of', 'IN'), ('voters', None), ('and', 'CC'), ('the', 'AT'), ('size', None), ('of', 'IN'), ('this', 'DT'), ('city', None), ("''", "''"), ('.', '.')]

# UnigramTagging dengan training

brown_tagged_Sents = brown.tagged_sents(categories='news')
brown_sents = brown_sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) # Train tagger berdasarkan data tagging
print unigram_Tagger.tag(brown_sents[2007])
print "###"

# N-Gram Tagging
# Pada Unigram Tagging, proses tagging dilihat hanya token per token saja.
# Tentu hal ini di dalam bahasa inggris akan menyulitkan, karena proses klasifikasi kata bisa dilakukan pada dua token sekaligus
# Misal: wind, the wind, to wind.

# Proses tagging yang memperhatikan konteks token sebelum disebut N-Gram Tagging







