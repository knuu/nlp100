import random
def typoglycemia(sentence):
    transformed = []
    for word in sentence.split():
        if len(word) > 4:
            head, middle, last = word[0], list(word[1:-1]), word[-1]
            random.shuffle(middle)
            word = head + ''.join(middle) + last
        transformed.append(word)
    return ' '.join(transformed)

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(sentence))
