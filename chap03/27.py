import re
with open('England.txt') as f:
    data = f.read()
    pat = re.compile(r"\{\{基礎情報 (.*?)\n\}\}", re.S)
    baseInfo = '\n'.join(pat.findall(data))
    emph = re.compile(r"(.*?)'+(.*?)'+(.*?)")
    baseInfo = emph.sub(lambda x: ''.join([x.group(i+1) for i in range(3)]) , baseInfo)
    insideLink = re.compile(r"\[\[(.*?)\]\]")
    baseInfo = insideLink.sub(lambda x: x.group(1), baseInfo)
    print(baseInfo)
    
    
