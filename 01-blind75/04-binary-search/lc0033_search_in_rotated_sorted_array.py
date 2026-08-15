"""
LC 33 — Search in Rotated Sorted Array | Medium | Binary Search
Pattern: which half is sorted, then check if target is in range
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    print("ok")
