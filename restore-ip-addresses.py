class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        self.helper(s,0,res,"")
        return res

    def helper(self,s,level,res,ip):
        if level == 4:
            if s == '':
                res.append(ip[1:])
            return
        for i in range(1,4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.helper(s[i:],level+1,res,ip+'.'+s[:i])
                if s[0] == '0':
                    break