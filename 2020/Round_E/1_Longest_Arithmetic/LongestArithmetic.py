t = int(input())
for i in range(1,t+1):
    for j in range(1):
        N = int(input())
        arithmetic = [int(s) for s in input().split(" ")]

        ans = []
        aux = arithmetic[0]
        for m in range(1,N):
            k = aux - arithmetic[m]
            ans.append(k)
            aux = arithmetic[m]
        
        ans2 = []
        aux2 = ans[0]
        count = 1
        for n in range(1,N-1):
            if aux2 == ans[n]:
                count = count +1
            else:
                ans2.append(count)
                count = 1

            aux2 = ans[n]

        ans2.append(count)

    print ( 'Case #{}: {}'.format(str(i),str(max(ans2)+1)) )