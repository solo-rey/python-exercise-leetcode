# @param s, a string
# @return a boolean
import re
def isNumber(s):
    if not s:
        return False
    s = s.strip()
    if len(s) == 0:
        return False
    dotFlag = False
    eFlag = False
    for i in range(len(s)):
        char = s[i]
        if char == '.':
            """
            1.no dot
            2. not e/E
            3. not the first or last char
            4. need to either first is a digit or last is a digit
            """
            if dotFlag or eFlag or (i == 0 or not s[i-1].isdigit()) and (i == len(s)-1 or not s[i+1].isdigit()):
                return False
            dotFlag = True
        elif char == '-' or char == '+':
            """
            1. appear first or after e/E
            2. next should be a digit
            """
            if((i >0 and s[i-1] != 'e' and s[i-1] != 'E') or (i == len(s)-1 or not (s[i+1].isdigit() or s[i+1] == '.'))):
                return False
        elif char == 'e' or char == 'E':
            if eFlag or i == len(s)-1 or i==0:
                """
                1. e/E not happen before
                2. not first
                3. not last
                """
                return False
            eFlag = True
        elif char.isdigit():
            continue
        else:
            return False
    return True


print isNumber("3.")