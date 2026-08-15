"""
LC 102 — Binary Tree Level Order Traversal | Medium | Trees
Pattern: BFS with for _ in range(len(q))
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def build(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q: deque[TreeNode] = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.levelOrder(build([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert s.levelOrder(build([1])) == [[1]]
    assert s.levelOrder(build([])) == []
    print("ok")
