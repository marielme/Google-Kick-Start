def count(x,y):
    return min(x//2,y)+min(y//2,x)-2

t = int(input())

for test in range(t):
    r, c = [int(x) for x in input().split()]
    matrix = []
    for k in range(r):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    top = [[0 for col in range(c)] for row in range(r)]
    left = [[0 for col in range(c)] for row in range(r)]
    botton = [[0 for col in range(c)] for row in range(r)]
    right = [[0 for col in range(c)] for row in range(r)]

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                top[i][j] = top[i - 1][j] + 1
                left[i][j] = left[i][j - 1] + 1

    for i in range(r):
        for j in range(c):
            if matrix[-i-1][-j-1] == 1:
                botton[-i-1][-j-1] = botton[-i-1 + 1][-j-1] + 1
                right[-i-1][-j-1] = right[-i-1][-j-1 + 1] + 1
  

    ans = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                ### Type 1: One of the segments is to top of (i,j), and other segment is to the right of (i,j).
                if top[i][j]>1 and right[i][j]>1:
                    ans += count(top[i][j],right[i][j])
    
                ### Type 2: One of the segments is to top of (i,j), and other segment is to the left of (i,j).
                if top[i][j]>1 and left[i][j]>1:
                    ans += count(top[i][j],left[i][j])

                ### Type 3: One of the segments is to bottom of (i,j)(i,j), and other segment is to the right of (i,j).
                if botton[i][j]>1 and right[i][j]>1:
                    ans += count(botton[i][j],right[i][j])
                    
                ### Type 4: One of the segments is to bottom of (i,j), and other segment is to the left of (i,j).
                if botton[i][j]>1 and left[i][j]>1:
                    ans += count(botton[i][j],left[i][j])

    print("Case #%d: %s" % (test+1, ans))