import math

t = int(input())

for j in range(1, t + 1):
    n,k = [int(x) for x in input().split(" ") ]
    arr = []
    for i in range(n):
        s,e = [int(x) for x in input().split(" ") ]
        arr.append((s,e))
    
    arr.sort()
    ans = 0
    point_time = 0

    for i in arr:
        point_time = max(point_time, i[0])
        while i[1] > point_time:
            count = math.ceil((i[1] - point_time) / k)
            ans += count
            point_time += count * k


    print("Case #{}: {}".format(j, ans))