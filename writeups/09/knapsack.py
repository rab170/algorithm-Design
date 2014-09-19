values = [3, 4, 6, 2]
weights = [4, 1, 2, 3]

print 'values = ', values
print 'weights = ', weights
print
MAX_SUM = max(values)*max(weights)
T = [[None for i in range(MAX_SUM*2)] for j in range(len(values)+1)]
T[0][0] = 0

for lvl, v_lvl in enumerate(values):
    w_lvl = weights[lvl]
    for w in range(0, MAX_SUM):
        if T[lvl][w] != None:
            T[lvl+1][w] = max(T[lvl+1][w], T[lvl][w])
            T[lvl+1][w + w_lvl] = max(T[lvl+1][w + w_lvl], T[lvl][w] + v_lvl)

max_row = 0
for i, row in enumerate(T):
    for j, val in enumerate(row):
        if j > max_row and val != None:
            max_row = j
        if val == None:
            T[i][j] = '_'

for i, row in enumerate(T):
    T[i] = row[:max_row+1]

s = [[str(e) for e in row] for row in T]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print '\n'.join(table)

