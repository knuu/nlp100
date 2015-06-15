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

with open('w.pickle', 'rb') as f1, open('feature_words.pickle', 'rb') as f2:
    w, feature_words = pickle.load(f1), pickle.load(f2)

with open('sentiment.txt') as f:
    data = f.readlines()
    s = [' '.join(data[i].split()[1:]) for i in range(20)]
    print(s)
for i in range(20):
    print(predict(w, make_feature_vector(s[i], feature_words)))

