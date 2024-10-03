class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = -1e9, prefix_sum = 0, min_prefix = 0;
        for (int num : nums) {
            prefix_sum += num;
            max_sum = max(max_sum, prefix_sum - min_prefix);
            min_prefix = min(min_prefix, prefix_sum);
        }
        return max_sum;

    }
};
