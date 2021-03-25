import numpy as np

# find the indices[i,j] of the maximum value in a 2d numpy array
def find_max(m):
    return np.unravel_index(np.argmax(m, axis=None), m.shape)


def update_neighbors(x,y,m,idx):
    cal = 0
   
    if m[x][y] < m[idx]-1:
        cal = (m[idx]-1) - m[x][y]
        m[x][y] = m[idx] -1
        
    return cal

def calculate_adjacent(m, idx, visit):
    R = idx[0]
    C = idx[1]
    top = 0
    botton =0
    left = 0
    right = 0
    
    if 0<=R-1 and visit[R-1][C] == 0: 
        top = update_neighbors(R-1,C,m,idx) 
        
    if R+1<len(m) and visit[R+1][C] == 0:
        botton = update_neighbors(R+1,C,m,idx)
    
    if 0<=C-1 and visit[R][C-1] == 0:
        left = update_neighbors(R,C-1,m,idx)
        
    if C+1<len(m[0]) and visit[R][C+1] == 0:
        right = update_neighbors(R,C+1,m,idx)
    
    return top + botton + left + right
     
    
t = int(input())

for i in range(t):
    r,c = [int(x) for x in input().split()]
    matrix=[]
    for j in range(r):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    
    m = np.array(matrix)   # create numpy array
    
    visit = np.array([[0 for col in range(c)] for row in range(r)])  # to store visited index 
    
    ans = 0
    
    while True:
        idx = find_max(m)
        visit[idx[0]][idx[1]] = 1
        ans += calculate_adjacent(m, idx, visit)
        m[idx[0]][idx[1]] = -1
        result = np.where(visit == 0)
        if len(result[0]) == 0:
            break
    
    print("Case #%d: %s" % (i+1, ans))
   