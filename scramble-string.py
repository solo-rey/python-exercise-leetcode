class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == 1 and len(s2) == 1:
            return s1[0] == s2[0]
        s3,s4 = s1[:],s2[:]
        s3.sort()
        s4.sort()
        if s1 == s2:
            return True
        if s3 != s4:
            return False
        for split in range(1,len(s1)):
            s11 = s1[0:split]
            s12 = s1[split]
            s21 = s2[0:split]
            s22 = s2[split]
            if self.isScramble(s11,s21) and self.isScramble(s12,s22):
                return True
            s21 = s2[0:len(s2)-split]
            s22 = s2[len(s2)-split:]
            if self.isScramble(s11,s22) and self.isScramble(s12,s21):
                return True
        return False
