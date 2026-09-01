class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 1. Transform each string into (# of 0, # of 1)
        zero_one_counts = []
        for s in strs:
            count_0, count_1 = 0, 0
            for ch in s:
                if ch == '0':
                    count_0 +=1
                else:
                    count_1 += 1
            zero_one_counts.append((count_0, count_1))

        # DP Table
        dp = [
            [[0] * (n + 1) for _ in range(m + 1)]
            for _ in range(len(strs) + 1)
        ]

        # Recursive Case
        for i in range(1, len(strs) + 1):
            zeros, ones = zero_one_counts[i - 1]
            for j in range(m + 1):
                for k in range(n + 1):
                    # Skip
                    dp[i][j][k] = dp[i - 1][j][k]

                    # Take
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i][j][k], 1 + dp[i - 1][j - zeros][k - ones])

        return dp[len(strs)][m][n]
