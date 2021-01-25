t = int(input())

for j in range(t):
    L = int(input())
    words = [x for x in input().split(" ")]
    s1, s2, n, a, b, c, d = [ x for x in input().split(" ")]
    N = int(n)
    A = int(a)
    B = int(b)
    C = int(c)
    D = int(d)

    ## Generate the string s

    s=['']*N
    s[0],s[1]=s1,s2
    x=[0]*N
    x[0],x[1]=ord(s1),ord(s2)
    for i in range(2,N):
        x[i] = (A*x[i-1]+B*x[i-2]+C)%D
        s[i]=chr(97+x[i]%26)
    s=''.join(s)

    ## find scrambled words
    ans = 0
    for ss in words:
        for i in range(len(s)-len(ss)+1):
            st = s[i:i+len(ss)]
            if st[0]==ss[0] and st[-1]==ss[-1] and (len(ss)<=2 or sorted(ss[1:-1])==sorted(st[1:-1])):
                ans+=1
                break

    print("Case #{}: {}".format(j+1, ans))

