with open("hightemp.txt") as f:
    pre, city = [], []
    for line in f.read().split('\n')[:-1]:
        pre_i, city_i, _, _ = line.split()
        pre.append(pre_i)
        city.append(city_i)
    with open("col1.txt", 'w') as f1:
        f1.write('\n'.join(pre))
    with open("col2.txt", 'w') as f2:
        f2.write('\n'.join(city))
