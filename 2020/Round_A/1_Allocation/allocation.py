t = int(input())

for i in range(1,t+1):
    for j in range(1):
        number_houses, budget = [int(s) for s in input().split(" ")]
        houses_prices = [int(s) for s in input().split(" ")]


    houses_prices.sort()
    sum_prices = 0
    maximun_number_houses = 0
    for k in houses_prices:
        sum_prices = sum_prices + k
        if sum_prices > budget:
            break
        else:
            maximun_number_houses = maximun_number_houses + 1
    print ( 'Case #{}: {}'.format(str(i),str(maximun_number_houses)) )