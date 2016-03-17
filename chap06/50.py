with open('nlp.txt') as f:
    lines = f.readlines()
sentences = []

for line in lines:
    s_start, cur = 0, 0
    end = len(line)
    while cur < end:
        s_start = cur
        while cur < end:
            if cur+2 < end and line[cur] in '.;:?!' and line[cur+1] in ' ' and line[cur+2].isupper():
                break
            cur += 1

        if line[s_start:cur+1].strip():
            sentences.append(line[s_start:cur+1].strip())
        cur += 2
print(*sentences, sep='\n')
with open('50.out', 'w') as f:
    f.write('\n'.join(sentences))

