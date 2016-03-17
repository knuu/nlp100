from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

with open('51.out') as f:
    words = [line.strip() for line in f.readlines()]
stem_words = [(word, stemmer.stem(word)) for word in words]
for word, stem in stem_words:
    print('{}\t{}'.format(word, stem))
