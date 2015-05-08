def zipStrings(astring1, astring2):
    return ''.join(s1+s2 for s1, s2 in zip(astring1, astring2))

if __name__ == '__main__':
    ans = zipStrings('パトカー', 'タクシー')
    print(ans)
