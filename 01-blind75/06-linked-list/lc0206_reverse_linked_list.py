"""
LC 206 — Reverse Linked List | Easy | Linked List
Pattern: prev / curr / nxt reverse in place
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseList(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(from_list([1, 2]))) == [2, 1]
    assert to_list(s.reverseList(from_list([]))) == []
    print("ok")
