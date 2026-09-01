class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(i, curr_sum):
            # Base Case
            if i == len(nums):
                return 1 if curr_sum == target else 0

            # Memoization
            state = (i, curr_sum)
            if state in memo:
                return memo[state]

            # Recursive Case: add or sub
            add_num = helper(i + 1, curr_sum + nums[i])
            sub_num = helper(i + 1, curr_sum - nums[i])

            memo[state] = add_num + sub_num
            return memo[state]

        return helper(0, 0)

