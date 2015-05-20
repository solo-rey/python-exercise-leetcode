class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr_old(self, haystack, needle):
        for i in range(len(haystack) - len(needle)-1):
            if haystack[i:i+len(needle)-1] == needle:
                return haystack[i:]
        return None


# @param haystack, a string
# @param needle, a string
# @return an integer
def strStr(haystack, needle):
    if needle == "": #"a",""
        return 0
    elif haystack == needle:
        return 0
    elif len(haystack) == len(needle):
        for i in range(len(haystack)):
            if haystack[i] != needle[i]:
                return -1
        return 0
    else:
        for i in range(len(haystack) - len(needle)+1): #"missippi","pi"
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

def strStr_good(haystack,needle):
    i,j = 0,0
    while True:
        j = 0
        while True:
            if j == len(needle):
                return i
            if i+j == len(haystack):
                return -1
            if needle[j] != haystack[i+j]:
                break
            j+=1
        i+=1



print strStr("aaa","aa")