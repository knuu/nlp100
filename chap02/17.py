with open("hightemp.txt") as f:
    lines = f.read().split('\n')[:-1]
    print('\n'.join(sorted(list(set([l.split()[0] for l in lines])))))
    
    
