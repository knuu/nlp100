import string

def countWordsAlphabet(asentense):
    words = asentense.split()
    alphabetListOfWords = [countAlphabet(w) for w in words]
    return alphabetListOfWords[:]

def countAlphabet(word):
    word = word.lower() # 大文字と小文字は区別しない
    alphabetList = [0] * 26
    for w in word:
        if w in string.ascii_lowercase:
            alphabetList[ord(w) - ord('a')] += 1
    return alphabetList[:]

if __name__ == '__main__':
    asentense = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    ans = countWordsAlphabet(asentense)
    for i in ans: print(i)
    
    

