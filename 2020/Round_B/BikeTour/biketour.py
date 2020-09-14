t = int(input())

for i in range(1,t+1):
    n = int(input())
    h = [int(s) for s in input().split(" ")]
    a=[x for x in range(1,len(h)-1) if h[x]>h[x-1] and h[x]>h[x+1]]
    print("Case #{}: {}".format(i,len(a)))