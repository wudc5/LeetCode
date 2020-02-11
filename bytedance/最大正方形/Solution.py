class Solution(object):
    def maximalSquare(self, matrix):
        M = len(matrix)
        if M == 0:
            return 0
        N = len(matrix[0])
        bp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        maxSqu = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if matrix[i - 1][j - 1] == "1":
                    bp[i][j] = min(bp[i - 1][j - 1], bp[i][j - 1], bp[i - 1][j]) + 1
                    maxSqu = max(maxSqu, bp[i][j])
        return maxSqu * maxSqu
