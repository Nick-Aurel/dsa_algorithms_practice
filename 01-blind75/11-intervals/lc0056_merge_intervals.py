"""
LC 56 — Merge Intervals | Medium | Intervals
Pattern: sort by start; merge if overlap
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    print("ok")
