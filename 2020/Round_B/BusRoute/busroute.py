t = int(input())

for i in range(1,t+1):
    for j in range(1):
        n , d = [int(s) for s in input().split(" ")]
        h = [int(s) for s in input().split(" ")]
        h.reverse()
        for j in h:
            if d%j !=0:
                d = d - (d%j)

    print("Case #{}: {}".format(i,d))