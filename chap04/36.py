from collections import Counter
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
#print(wordsRank[:10])
        
    
            
        
        
