"""
LC 572 — Subtree of Another Tree | Easy | Trees
Pattern: DFS + same-tree check
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.isSubtree(build([3, 4, 5, 1, 2]), build([4, 1, 2])) is True
    assert (
        s.isSubtree(build([3, 4, 5, 1, 2, None, None, None, None, 0]), build([4, 1, 2]))
        is False
    )
    print("ok")
