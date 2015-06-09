import re
with open('England.txt') as f:
    data = f.read()
    pat = re.compile(r'(==+)(.+?)(==+)')
    sections = pat.findall(data)
    for level, section, _ in sections:
        lev = len(level)-1
        print('\t'*(lev-1), section.lstrip(), lev)
    
