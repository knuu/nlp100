"""
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.xml')
root = tree.getroot()
sentences = []
for sentence in root.iter('sentence'):
    s = [word.text for word in sentence.iter('word')]
    if s: sentences.append(s)
for mention in root.iter('mention'):
    mention = {m.tag: m.text for m in mention.findall('*')}
    sid, start, end, text = mention['sentense']-1, mention['start'], mention['end'], mention['text']
    sentence = sentences[sid]
    
    sentences[sid] = sentence[:start] + text.split() 
print(*sentences, sep='\n')
"""
from bs4 import BeautifulSoup
with open('nlp.xml') as f:
    soup = BeautifulSoup(f.read(), "xml")

persons = [token.word.text for token in soup.find_all('token') if token.NER.text == 'PERSON']
print(*persons, sep='\n')
