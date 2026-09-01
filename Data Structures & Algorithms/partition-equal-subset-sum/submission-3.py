class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        target_sum = total_sum // 2
        if total_sum % 2:
            return False

        # Create DP table
        n = len(nums)
        dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

        # Base Case
        dp[0][0] = True

        for i in range(n + 1):
            curr_num = nums[i - 1]
            for j in range(1, target_sum + 1):
                if curr_num > j:
                    # cannot take the current number
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Take or skip the current number
                    dp[i][j] = dp[i - 1][j - curr_num] or dp[i - 1][j]

        return dp[n][target_sum]
