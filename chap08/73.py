from feature_extraction import *
import random, math, pickle

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def inner(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))  

def Logistic_regression(answer_data, max_iter=100, C=1.0, learning_rate=0.1, decrease=0.9):
    answers = answer_data[:]
    deg = len(answers[0][1])
    w = [0] * deg
    for _ in range(max_iter):
        random.shuffle(answers)

        for data in answers:
            x, y = data[1], data[0]
            predict = 1 - sigmoid(y * inner(w, x))
            for i in range(len(x)):
                regular = 2 * C/deg * w[i]
                w[i] = w[i] - learning_rate * (-y * predict * x[i] + regular)
            learning_rate *= decrease
    return w    

with open('feature_words.pickle', 'rb') as f:
    feature_words = pickle.load(f)
answer_data = feature_extraction('sentiment.txt', feature_words)
w = Logistic_regression(answer_data, max_iter=100)
with open('w.pickle', 'wb') as f:
    pickle.dump(w, f)
print(w)
