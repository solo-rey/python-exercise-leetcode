#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tao
#
# Created:     30/08/2014
# Copyright:   (c) tao 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def reverseWords(s):
    words = s.split()
    words.reverse()
    words = ' '.join(words)
    return words

print reverseWords("the sky is blue")