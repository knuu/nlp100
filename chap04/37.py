from collections import Counter
import pylab
with open('neko.txt.mecab') as f:
    mecabList = []
    sentenceList = [s for s in f.read().split('EOS\n') if s != '']
    for s in sentenceList:
        lineList = []
        for line in s.split('\n')[:-1]:
            surface, analysis = line.split('\t')
            morphInfo = analysis.split(',')
            lineList.append({'surface': surface, 'base': morphInfo[6], 'pos': morphInfo[0], 'pos1': morphInfo[1]})
        mecabList.append(lineList)

words = []
for line in mecabList:
    for morph in line:
        words.append(morph['surface'])
wordsRank = Counter(words).most_common()

pylab.figure()
words, cnts = [], []
top10 = 0
for word, cnt in wordsRank:
    if word in '。、「」':
        continue
    elif top10 == 10:
        break
    else:
        top10 += 1
    words.append(word)
    cnts.append(cnt)

quarters = pylab.arange(len(words))
width = 0.8
pylab.bar(quarters, cnts, width)
pylab.xticks(quarters+width/2, words)
pylab.title('The Top 10 words')
pylab.xlabel('Words')
pylab.ylabel('Counts')
pylab.show()
