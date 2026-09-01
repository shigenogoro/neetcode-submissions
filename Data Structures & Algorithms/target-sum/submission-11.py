class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Transform it into a subset sum problem
        # Divide them into positive set, and negative set
        #   - sum(P) + sum(N) == total_sum
        #   - sum(P) - sum(N) == target
        #   - Solve:    
        #       - 2 * sum(P) == total_sum + target
        #       - sum(P) = (total_sum + target) / 2
        #   - Find subset sum == (total_sum + target) / 2

        total_sum = sum(nums)
        
        # Invalid Check
        if abs(target) > total_sum or (total_sum + target) % 2 == 1:
            return 0

        new_target = (total_sum + target) // 2

        # DP Table
        n = len(nums)
        dp = [[0] * (new_target + 1) for _ in range(n + 1)]

        # Base Case:
        dp[0][0] = 1

        for i in range(1, n + 1):
            curr_num = nums[i - 1]
            for j in range(new_target + 1):
                if curr_num > j:
                    # Skip the curr_num
                    dp[i][j] = dp[i - 1][j]
                else:
                    # Take or skip the current number
                    dp[i][j] = dp[i - 1][j - curr_num] + dp[i - 1][j]

        return dp[n][new_target]