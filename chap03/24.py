import re
with open('England.txt') as f:
    data = f.read()
    pat = re.compile(r"ファイル:(.*?)\|")
    files = pat.findall(data)
    print('\n'.join(files))
