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

        memo = {}
        def helper(i, zeros, ones):
            # Base Case
            if i >= len(strs):
                return 0

            # Memoization
            state = (i, zeros, ones)
            if state in memo:
                return memo[state]

            curr_zero, curr_one = zero_one_counts[i]

            # Skip
            skip = helper(i + 1, zeros, ones)
            
            # Take
            take = 0
            if curr_zero + zeros <= m and curr_one + ones <= n:
                take = 1 + helper(i + 1, curr_zero + zeros, curr_one + ones)

            memo[state] = max(skip, take)
            return memo[state]

        ans = helper(0, 0, 0)
        return ans