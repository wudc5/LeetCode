class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0, len(height)-1
        maxLeft, maxRight = 0,0
        result = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    diff = maxLeft - height[left]
                    result += diff
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    diff = maxRight - height[right]
                    result += diff
                right -= 1
        return result