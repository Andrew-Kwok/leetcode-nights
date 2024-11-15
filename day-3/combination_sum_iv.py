class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        def F(N):
            if N < 0:
                return 0
            if N == 0:
                return 1
            if dp[N] != -1:
                return dp[N]

            dp[N] = 0
            for num in nums:
                dp[N] += F(N - num)
            return dp[N]
        
        return F(target)
