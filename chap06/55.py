"""
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.xml')
root = tree.getroot()
tokens = [token.find('word').text for token in root.iter('token') if token.find('NER').text == 'PERSON']
print(*tokens, sep='\n')
"""
from bs4 import BeautifulSoup
with open('nlp.xml') as f:
    soup = BeautifulSoup(f.read(), "xml")

persons = [token.word.text for token in soup.find_all('token') if token.NER.text == 'PERSON']
print(*persons, sep='\n')
