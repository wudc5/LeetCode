class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        recordMap = dict()
        for num in nums:
            if num not in recordMap.keys():
                left = recordMap.get(num - 1, 0)
                right = recordMap.get(num + 1, 0)
                recordMap[num] = right + left + 1
                if left != 0:
                    recordMap[num - left] = right + left + 1
                if right != 0:
                    recordMap[num + right] = right + left + 1
                if max < right + left + 1:
                    max = right + left + 1
        return max