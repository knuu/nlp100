"""
import xml.etree.ElementTree as ET
tree = ET.parse('nlp.xml')
root = tree.getroot()
words = [word.text for word in root.iter('word')]
print(*words, sep='\n')
"""
from bs4 import BeautifulSoup
with open('nlp.xml') as f:
    soup = BeautifulSoup(f.read(), "xml")

words = [word.text for word in soup.find_all('word')]
print(*words, sep='\n')

    
