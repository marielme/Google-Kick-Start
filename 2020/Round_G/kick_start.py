t = int(input())

for i in range(1, t+1):
    v = input()


    next = 0
    kicks = 0
    finder = True
    ans = 0
    while finder:
        kicks = v.find("KICK",next, len(v))
        ans += v.count("START", kicks, len(v))
        next = kicks + 1
        if kicks == -1:
           finder = False 

    print("Case #{}: {}".format(i, ans))
