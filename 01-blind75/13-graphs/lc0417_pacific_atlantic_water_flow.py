"""
LC 417 — Pacific Atlantic Water Flow | Medium | Graphs
Pattern: multi-source DFS/BFS from both oceans
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        raise NotImplementedError


def _as_set(cells: List[List[int]]) -> Set[Tuple[int, int]]:
    return {(r, c) for r, c in cells}


if __name__ == "__main__":
    s = Solution()
    got = _as_set(
        s.pacificAtlantic(
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    )
    expected = _as_set([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    assert got == expected
    assert _as_set(s.pacificAtlantic([[1]])) == {(0, 0)}
    print("ok")
