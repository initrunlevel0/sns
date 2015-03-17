from __future__ import division
import nltk, re, pprint
from nltk.corpus import names
import random, string

# Fitur ML pada NLTK

# NaiveBayesClassifier
# EXPERIMEN 1
# Klasifikasi nama cewek atau cowok berdasarkan huruf akhirnya (+ tambah fitur baru sekalian)

def gender_features(word):
    # Frequency of a..z
    word = word.lower()
    feature = {}
    for a in string.ascii_lowercase:
        feature[a + '_frequency'] = word.count(a)

#   feature['last_letter'] = word[-1]
#   feature['first_letter'] = word[0]
#   feature['length'] = len(word)

    return feature


# Data training dari corpus "names"
names = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')]

random.shuffle(names) # Acakacakacak

featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]  # Pisah data training dan data test (pecah 500, 500)

classifier = nltk.NaiveBayesClassifier.train(train_set)

# Uji coba
print classifier.classify(gender_features('Wira'))  # a: Female (doh)

# Lihat klasifikasi yang paling informative
classifier.show_most_informative_features(10)
print "###"

# EXPERIMEN 2
# Klasifikasi Dokumen: Melihat review film berdasarkan dia negatif atau positif

from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Ekstraksi fitur
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(20)
print "###"







