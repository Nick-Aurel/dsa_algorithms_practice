"""
LC 11 — Container With Most Water | Medium | Two Pointers
Pattern: opposite ends; move the shorter height
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    print("ok")
