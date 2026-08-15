"""
LC 143 — Reorder List | Medium | Linked List
Pattern: mid + reverse second half + merge
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def from_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    a = from_list([1, 2, 3, 4])
    s.reorderList(a)
    assert to_list(a) == [1, 4, 2, 3]
    b = from_list([1, 2, 3, 4, 5])
    s.reorderList(b)
    assert to_list(b) == [1, 5, 2, 4, 3]
    print("ok")
