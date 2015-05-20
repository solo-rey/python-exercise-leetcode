class Solution:
    """
    Given an array of strings, return all groups of strings that are anagrams.

    Note: All inputs will be in lower-case.
    """
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        anagram_map, res = {},[]
        for str in strs:
            sorted_str = ("").join(sorted(str))
            if sorted_str in anagram_map.keys():
                anagram_map[sorted_str].append(str)
            else:
                anagram_map[sorted_str] = [str]
        for anagram in anagram_map.values():
            if len(anagram) > 1:
                res += anagram
        return res

