with open('50.out') as f:
    sentences = f.readlines()
words = []

for sentence in sentences:
    sentence_words = []
    for word in sentence.split():
        if word[-1] in ',.':
            word = word[:-1]
        sentence_words.append(word)
    sentence_words.append('\n')
    words.extend(sentence_words)
print(''.join(map(lambda x: x+'\n' if x.strip() else x, words)))
with open('51.out', 'w') as f:
    f.write(''.join(map(lambda x: x+'\n' if x.strip() else x, words)))
    
