class Solution(object):
    def dfs(self, M, vis, i):
        for k in range(len(M)):
            if M[i][k] == 1 and vis[k] == 0:
                vis[k] = 1
                self.dfs(M, vis, k)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circle = 0
        num = len(M)
        if num == 0:
            return 0
        vis = [0] * num
        for i in range(num):
            if vis[i] == 0:
                vis[i] = 1
                self.dfs(M, vis, i)
                circle += 1
        return circle


