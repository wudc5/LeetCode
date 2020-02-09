class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        list1 = [0 for n in range(26)]
        list2 = [0 for n in range(26)]
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        for i in range(len1):
            list1[ord(s1[i]) - ord('a')] += 1
            list2[ord(s2[i]) - ord('a')] += 1
        for j in range(len1, len2):
            if list1 == list2:
                return True
            list2[ord(s2[j - len1]) - ord('a')] -= 1
            list2[ord(s2[j]) - ord('a')] += 1
        if list1 == list2:
            return True
        return False
