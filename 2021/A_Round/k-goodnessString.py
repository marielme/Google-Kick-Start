t = int(input())

for i in range(t):
    n, k = [int(x) for x in input().split(" ")]
    s = input()

    count = 0
    
    for j in range(n//2):
        if s[j] != s[n-j-1]:
            count += 1
            
    if count == k:
        ans = 0
    elif count > k:
        ans = count - k
    else:
        ans = k - count


    print("Case #%d: %s" % (i+1, ans))