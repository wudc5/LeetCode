class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sumSub = [0 for _ in range(len(nums))]
        sumSub[0] = nums[0]
        maxSub = nums[0]
        for i in range(1, len(nums)):
            sumSub[i] = max(sumSub[i - 1] + nums[i], nums[i])
            if maxSub < sumSub[i]:
                maxSub = sumSub[i]
        return maxSub