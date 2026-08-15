"""
LC 153 — Find Minimum in Rotated Sorted Array | Medium | Binary Search
Pattern: compare mid vs right to decide which half has the min
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    print("ok")
