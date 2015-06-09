import re
with open('England.txt') as f:
    data = f.read()
    pat = re.compile(r"\{\{基礎情報 (.*?)\n\}\}", re.S)
    baseInfo = '\n'.join(pat.findall(data))
    emph = re.compile(r"(.*?)'+(.*?)'+(.*?)")
    print(emph.sub(lambda x: ''.join([x.group(i+1) for i in range(3)]) , baseInfo))
    
