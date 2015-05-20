
def romanToInt(s):
    """
    From right to left,if dicit larger than previous add, otherwise subtract
    """
    dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    num = 0
    for i in reversed(range(len(s))):
        if i == len(s)-1 or dic[s[i]] >= dic[s[i+1]]:
            num += dic[s[i]]
        else:
            num -= dic[s[i]]
    return num


print romanToInt("MCMXCVI")