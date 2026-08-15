"""
LC 435 — Non-overlapping Intervals | Medium | Intervals
Pattern: greedy by end time
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("ok")
