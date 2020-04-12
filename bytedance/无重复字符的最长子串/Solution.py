#coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        start = 0
        dic = {}
        for i in range(len(s)):
            cur = s[i]
            if cur not in dic.keys():
                dic[cur] = i
            else:
                if dic[cur] + 1 > start:
                    start = dic[cur] + 1
                dic[cur] = i
            if i - start + 1 > maxLen:
                maxLen = i - start + 1
        return maxLen