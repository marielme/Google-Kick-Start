def even(x):
    n = str(x)
    respond = 1
    for i in n:
        if i not in ("0","2","4","6","8"):
            respond = 0
            break
    return respond

t = int(input())

for j in range(t):
    digit = input()

    digit_less = int(digit)
    digit_more = int(digit)
    ans = 0

    while True  :
        if even(digit_less) or even(digit_more):
            break
        ans += 1
        digit_less -= 1
        digit_more += 1

    print("Case #{}: {}".format(j+1, ans))
