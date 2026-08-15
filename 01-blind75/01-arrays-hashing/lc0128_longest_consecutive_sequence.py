"""
LC 128 — Longest Consecutive Sequence | Medium | Arrays & Hashing
Pattern: hash set; start a streak only when x-1 is missing
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    print("ok")
