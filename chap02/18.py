with open("hightemp.txt") as f:
    lines = f.read().split('\n')[:-1]
    ret = []
    for l in lines:
        pre, city, temp, date = l.split()
        ret.append((temp, pre, city, date))
    ret.sort()
    ret.reverse()
    print('\n'.join(['{}\t{}\t{}\t{}'.format(pre, city, temp, date) for temp, pre, city, date in ret]))

    
    
