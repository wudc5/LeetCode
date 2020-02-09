class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return result
        elif len(strs) == 1:
            return strs[0]
        else:
            firstStr = strs[0]
            for i in range(0, len(firstStr)):
                for j in range(1, len(strs)):
                    if len(strs[j]) <= i or firstStr[i] != strs[j][i]:
                        return result
                result += firstStr[i]
        return result
