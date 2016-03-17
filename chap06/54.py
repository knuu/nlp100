"""
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.xml')
root = tree.getroot()
tokens = ['{}\t{}\t{}'.format(token.find('word').text, token.find('lemma').text, token.find('POS').text) for token in root.iter('token') if not token.find('word').text in '.,']
print(*tokens, sep='\n')
"""
from bs4 import BeautifulSoup
with open('nlp.xml') as f:
    soup = BeautifulSoup(f.read(), "xml")

tokens = [(token.word.text, token.lemma.text, token.POS.text) for token in soup.find_all('token')]
for token in tokens:
    print('{}\t{}\t{}'.format(*token))
