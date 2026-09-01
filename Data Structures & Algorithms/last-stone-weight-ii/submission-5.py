class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Target: Find min(abs(2 * sum(A) - total_sum))
        #   -> Divide stones into 2 groups
        #   -> sum(A) + sum(B) == total_sum
        #   -> Find min(abs(sum(A) - sum(B)))
        #   -> sum(B) == total_sum - sum(A)
        #   -> i.e., We want to find min(abs(2 * sum(A) - total_sum))

        # 1. Get the total sum
        total_sum = sum(stones)

        # 2. DP
        n = len(stones)
        dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
        # Base Case
        dp[0][0] = True

        for i in range(1, n + 1):
            curr_stone = stones[i - 1]
            for j in range(total_sum + 1):
                # Skip
                skip = dp[i - 1][j]

                # Take
                take = False
                if curr_stone <= j:
                    take = dp[i - 1][j - curr_stone]

                dp[i][j] = skip or take

        # Find the subset sum closest to total_sum / 2
        for j in range(total_sum // 2, -1, -1):
            if dp[n][j]:
                return total_sum - 2 * j