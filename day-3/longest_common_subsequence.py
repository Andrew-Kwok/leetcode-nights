class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [[-1] * M for _ in range(N)]
                
        def F(i, j):
            if (i < 0 or j < 0) :
                return 0
                
            if (dp[i][j] != -1) :
                return dp[i][j]
            
            dp[i][j] = max(F(i-1, j), F(i, j-1))
            if (text1[i] == text2[j]) :
                dp[i][j] = max(dp[i][j], 1 + F(i-1, j-1))
            return dp[i][j]
            
        return F(N-1, M-1)
