class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        M = len(triangle)
        if M == 0:
            return 0
        dp = []
        for i in range(M):
            if i == 0:
                dp.append(triangle[M-1])
            else:
                tmp = [0 for _ in range(len(triangle[M-i-1]))]
                dp.append(tmp)
        for i in range(1,M):
            for j in range(len(dp[i])):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + triangle[M-i-1][j]
        return dp[M-1][0]
