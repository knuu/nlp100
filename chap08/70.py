import random
with open('rt-polarity.pos', encoding='"latin_1"') as pos, open('rt-polarity.neg', encoding='"latin_1"') as neg:
    posData = ['+1 {}'.format(line[:-1]) for line in pos.readlines()]
    negData = ['-1 {}'.format(line[:-1]) for line in neg.readlines()]
    data = posData + negData
    random.shuffle(data)

    with open('sentiment.txt', 'w', encoding='utf-8') as output:
        output.write('\n'.join(data))

with open('sentiment.txt') as f:
    pos, neg = 0, 0
    for line in f.readlines():
        if line.split()[0] == '+1':
            pos += 1
        else:
            neg += 1
    print('pos:\t{}\nneg:\t{}'.format(pos, neg))
    
    
    
    
    
