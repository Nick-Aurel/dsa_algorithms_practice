"""
LC 198 — House Robber | Medium | 1-D DP
Pattern: skip vs take; dp[i] = max(dp[i-1], dp[i-2] + nums[i])
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    print("ok")
