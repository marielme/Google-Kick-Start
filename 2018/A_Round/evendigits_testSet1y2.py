def call_previous_number (aux):
    if aux == "":
        aux += "20"
    else:    
        last_number = len(aux)
        previous_number = aux[last_number-1]
        aux = aux[:-1]
        if previous_number != "8":
            aux += str(int(previous_number)+2)
            return aux
        else:
            aux = call_previous_number(aux) + "0"
    return  aux

t = int(input())

for j in range(t):
    digit = input()

    aux = ""
    for i in range(len(digit)):
        if digit[i] in ("13579"):
            aux += str((int(digit[i])-1))
            aux += "8"*(len(digit)-i-1)
            break
        else:
            aux += digit[i]

    x = int(digit) - int(aux)

    aux = ""
    for i in range(len(digit)):
        if digit[i] in ("13579"):
            if digit[i] == "9":
                aux = call_previous_number(aux)
                aux += "0"*(len(digit)-i)
                break
            else:
                aux += str(int(digit[i])+1)
                aux += "0"*(len(digit)-i-1)
                break
        else:
            aux += digit[i]

    m = int(aux) - int(digit)

    ans = min(x,m)

    print("Case #{}: {}".format(j+1, ans))
