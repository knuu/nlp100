import sys
N = int(sys.argv[1])
with open('hightemp.txt') as f:
    print('\n'.join([line for line in f.read().split('\n')[-N-1:-1]]))

