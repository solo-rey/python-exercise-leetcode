# @return an integer
def atoi(str):
    maxdiv10 = 2147483647/10
    i,j = 0, len(str)
    while i < j and str[i] == ' ':
        i+=1
    sign = 1
    if i < j and str[i] == '+':
        i+=1
    elif i < j and str[i] == '-':
        i+=1
        sign = -1
    num = 0
    while i < j and str[i].isdigit():
        d = int(str[i])
        if num > maxdiv10 or num == maxdiv10 and d >= 8:
            if sign == 1:
                return 2147483647
            else:
                return -2147483648
        num = num*10+d
        i+=1
    return sign*num


def atoi1(str):
    maxint_10 = 2147483647
    i,j = 0 , len(str)
    while i != j:
        if str[i] == ' ':
            i+=1
            continue
        else:
            break
    sign = 1
    if i < j and str[i] == '+':
        i+=1
    elif i < j and str[i] == '-':
        i+=1
        sign=-1
    num = 0
    while i != j and str[i].isdigit():
        d = int(str[i])
        if num >= maxint_10:
            if sign == 1:
                return 2147483647
            else:
                return -2147483648
        num = num*10 + d
    return sign*num

print atoi1("010")




