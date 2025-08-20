#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
class Solution:        
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j], 
                            dp[i][j-1],     
                            dp[i-1][j-1]    
                        )
                        result = 0
        for i in range(m):
            for j in range(n):
                result += dp[i][j]
        return result

sol = Solution()
matrix = [
    [0, 1, 1],
    [1, 1, 1],
    [0, 1, 1]
]
print(sol.countSquares(matrix))