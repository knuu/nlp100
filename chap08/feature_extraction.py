from nltk.stem.porter import PorterStemmer
from collections import Counter

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

class Features:
    def __init__(self, cls1, cls2, top=200):
        self.cls1_top = dict(cls1.make_counter().most_common(top))
        self.cls2_top = dict(cls2.make_counter().most_common(top))
        self.feature_words = self.make_features(self.cls1_top, self.cls2_top) + self.make_features(self.cls2_top, self.cls1_top)

    def make_features(self, cls1_top, cls2_top):
        cnt = 0
        features = []
        for key in cls1_top.keys():
            if not key in cls2_top.keys():
                features.append(key)
                cnt += 1
        return features

def feature_extraction(data_path, feature):
    feature_vectors = []
    with open(data_path) as f:
        for line in f.readlines():
            words = line.split()
            words, cls = words[1:], int(words[0])
            feature_vector = [1 if f in words else 0 for f in feature.feature_words]
            feature_vectors.append((cls, feature_vector))
    return feature_vectors
