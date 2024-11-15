class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        def F(N):
            if N < 0:
                return math.inf
            if N == 0:
                return 0
            if dp[N] != -1:
                return dp[N]

            minCoin = min(F(N - coin) for coin in coins)
            if dp[N] != math.inf:
                minCoin += 1

            dp[N] = minCoin 
            return dp[N]

        minCoin = F(amount)
        return minCoin if minCoin != math.inf else -1
