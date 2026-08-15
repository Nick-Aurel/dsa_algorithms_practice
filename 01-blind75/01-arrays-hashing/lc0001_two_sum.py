"""
LC 1 — Two Sum | Easy | Arrays & Hashing
Pattern: hash map complement
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("ok")
