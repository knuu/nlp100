with open("hightemp.txt") as f:
    lines = f.read().split('\n')[:-1]
    dic = {}
    for l in lines:
        pre, _, _, _ = l.split()
        dic[pre] = dic.get(pre, 0) + 1
    pres = []
    for key in dic.keys():
        pres.append((dic[key], key))
    pres = sorted(pres, reverse=True)
    print('\n'.join([pre for cnt, pre in pres]))

    
    
