# @param num1, a string
# @param num2, a string
# @return a string
def multiply(num1, num2):
    num1,num2 = num1[::-1], num2[::-1]
    d = [0 for i in range(len(num1)+len(num2))]
    for i in range(len(num1)):
        a = int(num1[i])
        for j in range(len(num2)):
            b = int(num2[j])
            d[i+j] += a*b
    print d
    s = []
    for i in range(len(d)):
        digit = d[i] %10
        carry = d[i] / 10
        s.insert(0,str(digit))
        if i < len(d)-1:
            d[i+1]+=carry
    while len(s) > 1 and s[0] == '0':
        del s[0]
    return ''.join(s)


print multiply("123","456")