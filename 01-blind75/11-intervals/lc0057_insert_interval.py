"""
LC 57 — Insert Interval | Medium | Intervals
Pattern: left / overlap merge / right
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
    print("ok")
