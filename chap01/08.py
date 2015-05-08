import string

def cipher(c):
    changed = c
    if c in string.ascii_lowercase:
        changed = chr(219 - ord(c))
    return changed

def encodeCipher(astring):
    return ''.join([cipher(s) for s in astring])

def decodeCipher(astring):
    decoded = []
    for s in astring:
        if chr(219-ord(s)) in string.ascii_lowercase:
            decoded.append(chr(219-ord(s)))
        else:
            decoded.append(s)
    return ''.join(decoded)

if __name__ == '__main__':
    astring = 'This is a pen.'
    encoded = encodeCipher(astring)
    decoded = decodeCipher(encoded)
    print(astring, encoded, decoded)
