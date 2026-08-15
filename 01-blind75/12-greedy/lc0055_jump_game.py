"""
LC 55 — Jump Game | Medium | Greedy
Pattern: farthest reachable index
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
    print("ok")
