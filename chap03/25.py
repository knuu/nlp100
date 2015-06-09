import re
with open('England.txt') as f:
    data = f.read()
    pat = re.compile(r"\{\{基礎情報 (.*?)\n\}\}", re.S)
    baseInfo = '\n'.join(pat.findall(data))
    print(baseInfo)
    pat = re.compile(r"\|(.*?) = (.*)")
    Info = pat.findall(baseInfo)
    dic = {key: cont for key, cont in Info}
#    print(dic)
    
    
