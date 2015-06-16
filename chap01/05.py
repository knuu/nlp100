def make_ngram(n, token):
    return [tuple(token[i:i+n]) for i in range(len(token)-n+1)]

if __name__ == '__main__':
    sentence = "I am an NLPer"
    print(make_ngram(2, sentence.split()))
    print(make_ngram(2, list(sentence)))
