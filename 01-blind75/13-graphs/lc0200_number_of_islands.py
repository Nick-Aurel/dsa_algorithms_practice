"""
LC 200 — Number of Islands | Medium | Graphs
Pattern: DFS/BFS flood fill
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert (
        s.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        s.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
    print("ok")
