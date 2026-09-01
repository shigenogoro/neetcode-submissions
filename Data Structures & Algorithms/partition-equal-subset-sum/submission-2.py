class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        memo = {}
        def helper(i, set1_sum):
            set2_sum = total_sum - set1_sum
            # Base Case
            if  set1_sum == set2_sum:
                return True

            if i >= len(nums) or set1_sum > set2_sum:
                return False

            # Memoiztion
            state = (i, set1_sum)
            if state in memo:
                return memo[state]

            # Recursive Case: Take or Skip
            skip = helper(i + 1, set1_sum)
            take = helper(i + 1, set1_sum + nums[i])

            memo[state] = skip or take
            return memo[state]

        ans = helper(0, 0)
        return ans