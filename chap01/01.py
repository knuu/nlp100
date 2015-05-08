def pickString(astring, l):
    return ''.join([astring[i-1] for i in l])

if __name__ == '__main__':
    ans = pickString('パタトクカシーー', [1,3,5,7])
    print(ans)
