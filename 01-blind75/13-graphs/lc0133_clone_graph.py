"""
LC 133 — Clone Graph | Medium | Graphs
Pattern: map old node → new node (DFS or BFS)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from collections import deque
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def from_adj(adj: List[List[int]]) -> Optional[Node]:
    if not adj:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj) + 1)}
    for i, neigh in enumerate(adj, start=1):
        nodes[i].neighbors = [nodes[j] for j in neigh]
    return nodes[1]


def to_adj(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []
    seen: Dict[int, Node] = {}
    q: deque[Node] = deque([node])
    seen[node.val] = node
    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei.val not in seen:
                seen[nei.val] = nei
                q.append(nei)
    n = max(seen)
    return [[nbr.val for nbr in seen[i].neighbors] for i in range(1, n + 1)]


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    src = from_adj([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = s.cloneGraph(src)
    assert cloned is not src
    assert to_adj(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]
    empty = s.cloneGraph(None)
    assert empty is None
    print("ok")
