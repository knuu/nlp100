import sys
N =  int(sys.argv[1])
with open('hightemp.txt') as f:
    lines = f.read().split('\n')[:-1]
    splitline = [(i+1) * len(lines)//N for i in range(N)]
    for i in range(len(lines)%N):
        splitline[i] += 1
    splitline = [0] + splitline
    for i in range(N):
        with open('out_{}'.format(i), 'w') as fi:
            fi.write('\n'.join(lines[splitline[i]:splitline[i+1]]))


