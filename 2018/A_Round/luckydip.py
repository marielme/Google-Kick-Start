t = int(input())

for j in range(t):
    N, K = [int(x) for x in input().split(" ")]
    V = [int(x) for x in input().split(" ")]

    V.sort(reverse=True)

    E = sum(V)/N

    if max(V) != E:
        idx = 0
        newV = []
        for k in range(K):
            for i in range(N):
                if V[i] < E:
                    idx = i
                    break
            E = (sum(V[0:idx]) + E * (N-idx))/N


    print("Case #{}: {}".format(j+1, E))