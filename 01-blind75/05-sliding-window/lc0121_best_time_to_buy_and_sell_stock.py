"""
LC 121 — Best Time to Buy and Sell Stock | Easy | Sliding Window
Pattern: running minimum (one buy, one sell)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print("ok")
