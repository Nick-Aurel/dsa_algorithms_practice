"""
LC 226 — Invert Binary Tree | Easy | Trees
Pattern: DFS swap left/right
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


def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    out: List[Optional[int]] = []
    q: deque[Optional[TreeNode]] = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.invertTree(build([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert to_list(s.invertTree(build([2, 1, 3]))) == [2, 3, 1]
    assert to_list(s.invertTree(build([]))) == []
    print("ok")
