t = int(input())

for i in range(1,t+1):
    n = int(input())
    large_array = (n*2) -1
    list_to_sum = []
    
    for j in range(1,n+1):
        v = [ int(x) for x in input().split(" ")]
        aux = n - j
        while aux !=0:
            v.insert(0, 0)  #list.insert(pos, elmnt)
            aux -= 1
        
        while len(v)< large_array:
            v.extend([0])

        list_to_sum.append(v)


    list_with_sum = [sum(x) for x in zip(*list_to_sum)]

    ans = max(list_with_sum)

    print("Case #{}: {}".format(i, ans))
