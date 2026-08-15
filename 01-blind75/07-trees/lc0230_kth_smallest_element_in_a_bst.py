"""
LC 230 — Kth Smallest Element in a BST | Medium | Trees
Pattern: inorder traversal count
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.kthSmallest(build([3, 1, 4, None, 2]), 1) == 1
    assert s.kthSmallest(build([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    print("ok")
