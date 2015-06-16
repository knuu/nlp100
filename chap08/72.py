from nltk.stem.porter import PorterStemmer
from collections import Counter
import pickle

class SentenceData:
    def __init__(self, path, encode='utf-8'):
        self.sentences = []
        self.words = []
        with open(path, encoding=encode) as f:
            for line in f.readlines():
                sentence = self.stem_all(self.filter_stopwords(line.split()))
                self.sentences.append(sentence)
                self.words.extend(sentence)

    def filter_stopwords(self, sentence):
        with open('stop_words.txt', encoding='utf-8') as f:
            self.stop_words = f.readlines()[0].split()
        return list(filter(lambda word: not word in self.stop_words, sentence))

    def stem_all(self, sentence):
        stemmer = PorterStemmer()
        return [stemmer.stem(word) for word in sentence]
        
    def make_counter(self):
        return Counter(self.words)

def make_feature_words(cls1, cls2, top=2000):
    cls1_top = dict(cls1.make_counter().most_common(top//2))
    cls2_top = dict(cls2.make_counter().most_common(top//2))
    return list(set(list(cls1_top.keys()) + list(cls2_top.keys())))

def feature_extraction(data_path, feature_words):
    feature_vectors = []
    with open(data_path) as f:
        for line in f.readlines():
            words = line.split()
            words, cls = words[1:], int(words[0])
            feature_vector = [1 if f in words else 0 for f in feature_words]
            feature_vectors.append((cls, feature_vector))
    return feature_vectors

pos = SentenceData('rt-polarity.pos', encode='ISO-8859-1')
neg = SentenceData('rt-polarity.neg', encode='ISO-8859-1')
feature_words = make_feature_words(pos, neg)
with open('feature_words.pickle', 'wb') as f:
    pickle.dump(feature_words, f)
answer_data = feature_extraction('sentiment.txt', feature_words)

#print(len(feature_words))
#print(answer_data[0])
#print(sum(answer_data[0][1]))
