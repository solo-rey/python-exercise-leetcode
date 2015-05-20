# @return a string
def intToRoman(num):
    symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    i = 0
    st = ""
    while num != 0 and i <= len(values):
        if (num - values[i]) >= 0:
            num -= values[i]
            st += symbols[i]
        else:
            i+=1
    return st

print intToRoman(1990)

