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


nounPhrase = []
for line in mecabList:
    for i in range(1,len(line)-1):
        if line[i-1]['pos'] == '名詞' and line[i]['surface'] == 'の' and line[i]['pos1'] == '連体化' and line[i+1]['pos'] == '名詞':
            nounPhrase.append('{}{}{}'.format(line[i-1]['surface'], line[i]['surface'], line[i+1]['surface']))
print(nounPhrase)

            
        
        
