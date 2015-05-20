# @param s, a string
# @return an integer
def numDecodings(s):
    if not s or len(s) == 0 or s[0] == '0':
        return 0
    num1 = 1 #means res[i-2], combine two digits to decode
    num2 = 1 #means res[i-1], combine one digit to decode
    num3 = 1
    for i in range(1,len(s)):
        if s[i] == '0':
            if s[i-1] == '0':
                return 0
            elif s[i-1] == '1' or s[i-1] == '2':
                num3 = num1
            else:
                return 0
        else:
            if s[i-1] == '0' or s[i-1] >= '3':
                num3 = num2
            elif s[i-1] == '2' and s[i] >= '7' and s[i] <= '9':
                num3 = num2
            else:
                num3 = num1 + num2
        num1=num2
        num2=num3
    return num2

print numDecodings("11")