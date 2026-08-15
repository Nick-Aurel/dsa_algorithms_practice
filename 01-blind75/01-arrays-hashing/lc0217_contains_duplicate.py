"""
LC 217 — Contains Duplicate | Easy | Arrays & Hashing
Pattern: hash set membership
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("ok")
