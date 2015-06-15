import pickle, math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def inner(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))  

def make_feature_vector(sentence, feature_words):
    words = sentence.split()
    return  [1 if f in words else 0 for f in feature_words]

def predict(w, feature_vector):
    prob = sigmoid(inner(w, feature_vector))
    label = 1 if prob >= 0.5 else -1
    return label, prob

class DataScore:
    def __init__(self, data):
        self.num_data = len(data)
        self.true_pos = 0
        self.false_pos = 0
        self.true_neg = 0
        self.false_neg = 0
        for ans, pre, _ in data:
            if pre == 1 and ans == 1:
                self.true_pos += 1
            elif pre == 1 and ans == -1:
                self.false_pos += 1
            elif pre == -1 and ans == 1:
                self.true_neg += 1
            elif pre == -1 and ans == -1:
                self.false_neg += 1

    def accuracy(self):
        return (self.true_pos + self.false_neg) / self.num_data

    def precision(self):
        return self.true_pos / (self.true_pos + self.false_pos)

    def recall(self):
        return self.true_pos / (self.true_pos + self.false_neg)

    def f1(self):
        return 2 * self.precision() * self.recall() / (self.precision() + self.recall())        
        
with open('w.pickle', 'rb') as f1, open('feature_words.pickle', 'rb') as f2:
    w, feature_words = pickle.load(f1), pickle.load(f2)

predict_data = []
with open('sentiment.txt') as f:
    for data in f.readlines():
        data = data.split()
        ans, sentence = int(data[0]), ' '.join(data[1:])
        pre, prob = predict(w, make_feature_vector(sentence, feature_words))
        predict_data.append((ans, pre, prob))

score = DataScore(predict_data)
print('accuracy: {}'.format(score.accuracy()))
print('precision: {}'.format(score.precision()))
print('recall: {}'.format(score.recall()))
print('f1 score: {}'.format(score.f1()))
