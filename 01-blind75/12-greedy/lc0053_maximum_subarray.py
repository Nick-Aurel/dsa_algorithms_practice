"""
LC 53 — Maximum Subarray | Medium | Greedy
Pattern: Kadane (local choice + running max)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    print("ok")
