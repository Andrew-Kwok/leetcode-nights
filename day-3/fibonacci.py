class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def F(N):
            if N <= 1:
                return 1
            if dp[N] != -1:
                return dp[N]
            dp[N] = F(N-1) + F(N-2)
            return dp[N]
        return F(n)
