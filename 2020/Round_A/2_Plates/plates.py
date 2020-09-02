t = int(input())

for i in range(1,t+1):
    plates =[]
    for j in range(1):
        N, K, P  = [int(s) for s in input().split(" ")]
        for k in range(N):
            stacks = [int(s) for s in input().split(" ")]
            plates.append(stacks)
        print(plates)
        sum = 0
        for l in plates:
            max_bauty = max(l)
            count_max = [i for i,x in enumerate(l) if x==max_bauty]
            if P >= count_max[-1]+1:
                for i in range(count_max[-1]+1):
                    sum = sum + l[i]
                    P = P-1
        cont = 1
        rest = plates[-1]
        while P != 0:
            sum = sum + rest[count_max[-1]+cont]
            P = P-1
            cont = cont +1

                    
   
    print ( 'Case #{}: {}'.format(str(i),str(sum)) )