"""
LC 213 — House Robber II | Medium | 1-D DP
Pattern: circular = rob range [0..n-2] vs [1..n-1]
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([1, 2, 3]) == 3
    print("ok")
