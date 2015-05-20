class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res = []
        if words is None or len(words) == 0:
            return res
        count,last = 0,0
        for i in range(len(words)):
            if count+len(words[i])+(i-last) > L:
                spacenum = 0
                extranum = 0
                if i-last-1 > 0: #could be a case where a single word with length L,so no space needs to applicate in this case
                    spacenum = (L-count) / (i-last-1)
                    extranum = (L-count) % (i-last-1)
                st = ""
                for j in range(last,i):
                    #add all the words from last to i
                    #last indicate the first word in this line
                    st += words[j]
                    if j < i-1:
                        #no need to add space after the last word
                        for k in range(spacenum):
                            st += " "
                        if extranum > 0:
                            st += " "
                        extranum-=1
                for j in range(len(st),L):
                    st+=" "
                res.append(st)
                count=0
                last=i
            count+=len(words[i])
        st = ""
        for i in range(last,len(words)):
            st+=words[i]
            if len(st) < L:
                st+=" "
        for i in range(len(st),L):
            st+=" "
        res.append(st)
        return res
