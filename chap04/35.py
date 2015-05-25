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

longestNounPhrase = []
for line in mecabList:
    i = 0
    while i < len(line):
        if line[i]['pos'] == '名詞':
            longNounPhrase = ''
            while i < len(line) and line[i]['pos'] == '名詞':
                longNounPhrase += line[i]['surface']
                i += 1
            longestNounPhrase.append(longNounPhrase)
        i += 1
print(longestNounPhrase)

            
        
        
