import json
with open('jawiki-country.json', encoding='utf-8') as f:
    data = [json.loads(line) for line in f]
text = []
for d in data:
    if 'イギリス' in d['title']:
        text.append(d['text'])
text = '\n'.join(text)
with open('England.txt', 'w') as f:
    f.write(text)

