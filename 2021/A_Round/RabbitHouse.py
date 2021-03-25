    
t = int(input())

for k in range(t):
    ans = 0
    r,c = [int(x) for x in input().split()]
    G=[]
    for j in range(r):
        row = [int(x) for x in input().split()]
        G.append(row)
        ans -= sum(row)
        
    for i in range(r):
        for j in range(1,c):
            G[i][j] = max(G[i][j], G[i][j-1]-1)
        for j in range(c-1):
            G[i][c-j-2] = max(G[i][c-j-2], G[i][c-j-1]-1)
            
    for i in range(1,r):
        for j in range(c):
            G[i][j] = max(G[i][j], G[i-1][j]-1)
    
    for i in range(r-1):
        for j in range(c):
            G[r-i-2][j] = max(G[r-i-2][j], G[r-i-1][j]-1)
            
    for i in range(r):
        for j in range(c):
            ans +=G[i][j]
    
    
    print("Case #%d: %s" % (k+1, ans))
   