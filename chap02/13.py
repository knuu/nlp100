with open("col1.txt") as f1, open("col2.txt") as f2:
    ret = ['{}\t{}'.format(p, c) for p, c in zip(f1.read().split('\n'), f2.read().split('\n'))]
    with open("col3.txt", 'w') as f3:
        f3.write('\n'.join(ret))

