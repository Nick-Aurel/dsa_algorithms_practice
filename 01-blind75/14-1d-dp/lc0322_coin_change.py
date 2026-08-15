"""
LC 322 — Coin Change | Medium | 1-D DP
Pattern: unbounded knapsack min coins
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    print("ok")
