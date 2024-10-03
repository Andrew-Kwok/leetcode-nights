class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, prefix_sum, min_prefix = -1e9, 0, 0
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_prefix)
            min_prefix = min(min_prefix, prefix_sum)
        return max_sum
