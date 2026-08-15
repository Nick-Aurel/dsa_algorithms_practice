"""
LC 15 — 3Sum | Medium | Two Pointers
Pattern: sort + fixed i + two-sum; skip duplicates
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        raise NotImplementedError


def _normalized(triplets: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(t) for t in triplets)


if __name__ == "__main__":
    s = Solution()
    assert _normalized(s.threeSum([-1, 0, 1, 2, -1, -4])) == _normalized(
        [[-1, -1, 2], [-1, 0, 1]]
    )
    assert s.threeSum([0, 1, 1]) == []
    assert _normalized(s.threeSum([0, 0, 0])) == [[0, 0, 0]]
    print("ok")
