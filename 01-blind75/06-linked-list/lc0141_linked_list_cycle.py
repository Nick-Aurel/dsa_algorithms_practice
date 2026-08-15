"""
LC 141 — Linked List Cycle | Easy | Linked List
Pattern: Floyd slow / fast pointers
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def from_list_with_cycle(vals: List[int], pos: int) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    nodes: List[ListNode] = []
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
        nodes.append(tail)
    if pos >= 0 and nodes:
        tail.next = nodes[pos]
    return dummy.next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert s.hasCycle(from_list_with_cycle([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(from_list_with_cycle([1, 2], 0)) is True
    assert s.hasCycle(from_list_with_cycle([1], -1)) is False
    print("ok")
