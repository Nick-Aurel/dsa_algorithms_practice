"""
LC 39 — Combination Sum | Medium | Backtracking
Pattern: choose / explore / unchoose; reuse index i
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        raise NotImplementedError


def _normalized(combos: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(c) for c in combos)


if __name__ == "__main__":
    s = Solution()
    assert _normalized(s.combinationSum([2, 3, 6, 7], 7)) == _normalized(
        [[2, 2, 3], [7]]
    )
    assert _normalized(s.combinationSum([2, 3, 5], 8)) == _normalized(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
    assert s.combinationSum([2], 1) == []
    print("ok")
