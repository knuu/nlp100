def make_ngram(n, token):
    return [tuple(token[i:i+n]) for i in range(len(token)-n+1)]

if __name__ == '__main__':
    word1, word2 = "paraparaparadise", "paragraph"
    X, Y = set(make_ngram(2, list(word1))), set(make_ngram(2, list(word2)))
    print('Union: {}'.format(X | Y))
    print('Intersection: {}'.format(X & Y))
    print('Difference: {}'.format(X - Y))
    print('"se" in X: {}'.format(tuple('se') in X))
    print('"se" in Y: {}'.format(tuple('se') in Y))
