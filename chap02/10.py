with open('hightemp.txt') as f:
    print(len(f.read().split('\n')[:-1]))
