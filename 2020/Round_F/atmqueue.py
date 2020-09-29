import math
t = int(input())

for j in range(1, t + 1):
    n,q = [int(x) for x in input().split(" ") ]
    arr = []
    ans = []
    for index, a in enumerate(input().split(" "), start= 1):
        arr.append([math.ceil(int(a)/q), index])

    arr.sort(key=lambda x:  x[0])

    for i in arr:
        ans.append(i[1])

    print("Case #{}: ".format(j), *ans)
