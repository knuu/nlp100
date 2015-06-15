import pickle

with open('w.pickle', 'rb') as f1, open('feature_words.pickle', 'rb') as f2:
    w, feature_words = pickle.load(f1), pickle.load(f2)

ranked_features = sorted((w, f) for w, f in zip(w, feature_words))
print('[last10]')
for i, (w, f) in enumerate(ranked_features[:10]):
    print('{}. {} {}'.format(i+1, f, w))
print('[top10]')
for i, (w, f) in enumerate(ranked_features[-10:]):
    print('{}. {} {}'.format(i+1, f, w))
