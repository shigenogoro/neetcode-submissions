class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Transform it into subset sum problem
        # Divide stones into positive and negative groups
        #   -> Find min(abs(sum(P) - sum(N)))
        #   -> total_sum = sum(P) + sum(N)
        #   -> sum(N) = total_sum - sum(P)
        #   -> Find min(abs(2 * sum(P) - total_sum))

        # Step 1: Find the total sum
        total_sum = sum(stones)
        
        # Memoization
        memo = {}
        def helper(i, curr_sum):
            if i >= len(stones):
                return abs(2 * curr_sum - total_sum)

            # Memoization
            state = (i, curr_sum)
            if state in memo:
                return memo[state]

            # Skip or Take the current stone
            skip = helper(i + 1, curr_sum)
            take = helper(i + 1, curr_sum + stones[i])

            memo[state] = min(skip, take)
            return memo[state]

        ans = helper(0, 0)
        return ans