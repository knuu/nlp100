with open('England.txt') as f:
    for line in f.readlines():
        if 'Category' in line:
            print(line[:-1])
