from __future__ import division
import nltk, re, pprint

# Open Gutenberg
text = open("2554.txt", "r").read()

# TOKENIZE
# Definisi: Memisahkan sebuah bagian teks menjadi bagian-bagian unit tertentu.
# Tidak mesti dibagi per kata, karena pembagian dilakukan untuk memisahkan unit semantikna.
# http://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html

# nltk.word_tokenize: Memisahkan token berbasis kata
tokens = nltk.word_tokenize(text)

# Vocabulary
# Get list of vocabulary inside

words = [w.lower() for w in tokens]
vocab = sorted(set(words))


# STEMMER
# Definisi: Mendapatkan kata dasar (stem) dari sebuah kata.
# Nltk menyediakan dua jenis stemmer :
# * nltk.PorterStemmer()
# * nltk.LancasterStemmer()
# * nltk.WordNetLemmatizer()

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
stem_porter = [porter.stem(t) for t in tokens]
stem_lancaster = [lancaster.stem(t) for t in tokens]
print stem_lancaster
