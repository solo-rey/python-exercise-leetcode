"""
Given two (dictionary) words as Strings, determine if they are isomorphic.

Two words are called isomorphic if the letters in one word can be remapped to get the second word.

Remapping a letter means replacing all occurrences of it with another letter while the ordering of the letters remains unchanged.

No two letters may map to the same letter, but a letter may map to itself.

 Example:

given "foo", "app"; returns true we can map f -> a and o->p
given "bar", "foo"; returns false we can't map both 'a' and 'r' to 'o'
given "ab", "ca"; returns true we can map 'a' -> 'b' and 'c' -> 'a'



"""


def check_isomorphic(s,t):
    if len(s) != len(t):
        return False
    if s is None and t is None:
        return True
    if (s is None and not t) or (not s and t):
        return False
    map1,map2 = {},{}
    for i in range(len(s)):
        if s[i] in map1:
            if map1[s[i]] != t[i]:
                return False
        if t[i] in map2:
            if map1[t[i]] != s[i]:
                return False
        map1[s[i]] = t[i]
        map2[t[i]] = s[i]
    return True
