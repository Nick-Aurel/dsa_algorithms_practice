"""
LC 21 — Merge Two Sorted Lists | Easy | Linked List
Pattern: dummy head + tail merge
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.mergeTwoLists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [
        1,
        1,
        2,
        3,
        4,
        4,
    ]
    assert to_list(s.mergeTwoLists(from_list([]), from_list([]))) == []
    assert to_list(s.mergeTwoLists(from_list([]), from_list([0]))) == [0]
    print("ok")
