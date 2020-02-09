#coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = dict()
        i = 0
        maxLen = 0
        for j in range(len(s)):
            if s[j] in index.keys():
                i = max(index[s[j]], i)
            maxLen = max(maxLen, j-i+1)
            index[s[j]] = j+1
        return maxLen