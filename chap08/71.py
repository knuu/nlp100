import doctest
def isStopWord(word):
    """
    check if the word is in stop list
    >>> isStopWord('a')
    True
    >>> isStopWord('apple')
    False
    """
    return word in stop_words        

with open('stop_words.txt') as f:
    stop_words = f.readlines()[0].split()

if __name__ == '__main__':
    doctest.testmod()
