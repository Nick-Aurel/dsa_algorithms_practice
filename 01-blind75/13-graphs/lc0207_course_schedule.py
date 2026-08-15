"""
LC 207 — Course Schedule | Medium | Graphs
Pattern: cycle detect (3-color DFS) or Kahn topo
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) is True
    assert s.canFinish(2, [[1, 0], [0, 1]]) is False
    print("ok")
