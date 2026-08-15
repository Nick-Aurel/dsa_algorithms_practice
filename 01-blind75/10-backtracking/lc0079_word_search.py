"""
LC 79 — Word Search | Medium | Backtracking
Pattern: grid DFS + in-place mark
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert s.exist([row[:] for row in board], "ABCCED") is True
    assert s.exist([row[:] for row in board], "SEE") is True
    assert s.exist([row[:] for row in board], "ABCB") is False
    print("ok")
