def elementNumber(astring, l):
    elementDic = {}
    for i, s in enumerate(astring.split()):
        end = 2
        if i+1 in l:
            end = 1
        elementDic[s[:end]] = i+1
    return elementDic

if __name__ == '__main__':
    astring = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    ans = elementNumber(astring, [1,5,6,7,8,9,15,16,19])
    print(ans)
    
