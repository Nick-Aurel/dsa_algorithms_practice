"""
LC 235 — Lowest Common Ancestor of a Binary Search Tree | Medium | Trees
Pattern: walk by value (both < go left, both > go right)
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


def find(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find(root.left, val) or find(root.right, val)


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    root = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert root is not None
    p, q = find(root, 2), find(root, 8)
    assert p is not None and q is not None
    assert s.lowestCommonAncestor(root, p, q).val == 6
    p, q = find(root, 2), find(root, 4)
    assert p is not None and q is not None
    assert s.lowestCommonAncestor(root, p, q).val == 2
    print("ok")
