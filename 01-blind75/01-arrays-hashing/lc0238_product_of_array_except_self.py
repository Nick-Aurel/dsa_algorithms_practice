"""
LC 238 — Product of Array Except Self | Medium | Arrays & Hashing
Pattern: prefix / suffix products (no division)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("ok")
