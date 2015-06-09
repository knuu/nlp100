import re
with open('England.txt') as f:
    for line in f.readlines():
        if 'Category' in line:
            pat = re.compile(r"\[\[Category:(.*?)(\|.*){0,1}\]\]")
            valid = pat.match(line)
            print(valid.group(1))
