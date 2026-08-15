"""
DSA interview templates (Python 3).

Write these from memory during Hour 0. If you cannot reproduce a snippet
without looking, you cannot use it under interview pressure.

These are skeletons — not problem solutions. Fill in / re-type, then start Blind 75.
"""

from __future__ import annotations

import heapq
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set


# ---------------------------------------------------------------------------
# Hash map / set
# ---------------------------------------------------------------------------

def frequency_map(items: List[int]) -> Dict[int, int]:
    """Count occurrences. Also: Counter(items)."""
    counts: Dict[int, int] = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    return counts


def complement_lookup(nums: List[int], target: int) -> Optional[tuple[int, int]]:
    """For each x, look up target - x in a seen map of value -> index."""
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    return None


# ---------------------------------------------------------------------------
# Two pointers
# ---------------------------------------------------------------------------

def two_pointers_opposite(arr: List[int]) -> None:
    """Sorted array: move the pointer that can improve the pair."""
    l, r = 0, len(arr) - 1
    while l < r:
        # if too small: l += 1
        # if too large: r -= 1
        # if equal / valid: record, then l += 1 and/or r -= 1
        l += 1  # placeholder so the skeleton runs


def two_pointers_same_direction(arr: List[int]) -> None:
    """Slow/fast or read/write: slow trails, fast scans."""
    slow = 0
    for fast in range(len(arr)):
        # if arr[fast] should be kept: arr[slow] = arr[fast]; slow += 1
        _ = fast
        _ = slow


# ---------------------------------------------------------------------------
# Stack
# ---------------------------------------------------------------------------

def stack_matching(s: str) -> bool:
    """Push openers; pop on closers. Empty stack at end => valid."""
    pairs = {")": "(", "]": "[", "}": "{"}
    st: List[str] = []
    for ch in s:
        if ch in pairs:
            if not st or st[-1] != pairs[ch]:
                return False
            st.pop()
        else:
            st.append(ch)
    return not st


def monotonic_stack(arr: List[int]) -> List[int]:
    """Next greater element to the right. Increasing stack of indices."""
    n = len(arr)
    ans = [-1] * n
    st: List[int] = []
    for i, x in enumerate(arr):
        while st and arr[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans


# ---------------------------------------------------------------------------
# Queue / deque
# ---------------------------------------------------------------------------

def bfs_queue(start: int, adj: Dict[int, List[int]]) -> List[int]:
    """Level-order walk. Use deque — never list.pop(0)."""
    q: deque[int] = deque([start])
    seen: Set[int] = {start}
    order: List[int] = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj.get(node, []):
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    return order


# ---------------------------------------------------------------------------
# Linked list
# ---------------------------------------------------------------------------

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def dummy_head_pattern(head: Optional[ListNode]) -> Optional[ListNode]:
    """Dummy simplifies insert/delete at the real head."""
    dummy = ListNode(0, head)
    _ = dummy.next  # operate from dummy
    return dummy.next


def slow_fast(head: Optional[ListNode]) -> Optional[ListNode]:
    """Midpoint / cycle detection. Fast moves 2, slow moves 1."""
    slow = fast = head
    while fast and fast.next:
        assert slow is not None
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_two_sorted(
    a: Optional[ListNode], b: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


# ---------------------------------------------------------------------------
# Binary tree DFS / BFS
# ---------------------------------------------------------------------------

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


def dfs_recursive(root: Optional[TreeNode]) -> None:
    if not root:
        return
    dfs_recursive(root.left)
    dfs_recursive(root.right)


def dfs_iterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    st: List[TreeNode] = [root]
    order: List[int] = []
    while st:
        node = st.pop()
        order.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return order


def bfs_levels(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    q: deque[TreeNode] = deque([root])
    levels: List[List[int]] = []
    while q:
        level: List[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(level)
    return levels


# ---------------------------------------------------------------------------
# Graph: adj list, DFS, BFS, Kahn topo
# ---------------------------------------------------------------------------

def build_adj(n: int, edges: List[List[int]], directed: bool = False) -> List[List[int]]:
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def graph_dfs(n: int, adj: List[List[int]]) -> List[int]:
    seen = [False] * n
    order: List[int] = []

    def dfs(u: int) -> None:
        seen[u] = True
        order.append(u)
        for v in adj[u]:
            if not seen[v]:
                dfs(v)

    for u in range(n):
        if not seen[u]:
            dfs(u)
    return order


def has_cycle_directed(n: int, adj: List[List[int]]) -> bool:
    """0 = unvisited, 1 = visiting (on stack), 2 = done."""
    state = [0] * n

    def dfs(u: int) -> bool:
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    return any(state[u] == 0 and dfs(u) for u in range(n))


def kahn_topo(n: int, adj: List[List[int]]) -> Optional[List[int]]:
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    q: deque[int] = deque([u for u in range(n) if indeg[u] == 0])
    order: List[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else None  # None => cycle


# ---------------------------------------------------------------------------
# Binary search
# ---------------------------------------------------------------------------

def binary_search_exact(arr: List[int], target: int) -> int:
    """Return index of target or -1. arr must be sorted."""
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binary_search_first_true(lo: int, hi: int, predicate) -> int:
    """Smallest x in [lo, hi] where predicate(x) is True. hi is inclusive.
    Caller must guarantee a True exists, or check after.
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ---------------------------------------------------------------------------
# Sliding window
# ---------------------------------------------------------------------------

def variable_window(s: str) -> int:
    """Grow r; shrink l while the window is invalid. Track counts."""
    counts: Dict[str, int] = defaultdict(int)
    l = 0
    best = 0
    for r, ch in enumerate(s):
        counts[ch] += 1
        while False:  # replace with "window invalid"
            counts[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best


# ---------------------------------------------------------------------------
# Heap
# ---------------------------------------------------------------------------

def top_k_min_heap(nums: List[int], k: int) -> List[int]:
    """k largest: keep a min-heap of size k."""
    heap: List[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap


def max_heap_push(heap: List[int], x: int) -> None:
    """heapq is a min-heap. Negate for max-heap."""
    heapq.heappush(heap, -x)


def max_heap_pop(heap: List[int]) -> int:
    return -heapq.heappop(heap)


# ---------------------------------------------------------------------------
# Backtracking
# ---------------------------------------------------------------------------

def backtrack_subsets(nums: List[int]) -> List[List[int]]:
    ans: List[List[int]] = []
    path: List[int] = []

    def dfs(i: int) -> None:
        if i == len(nums):
            ans.append(path[:])
            return
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
        dfs(i + 1)

    dfs(0)
    return ans


def backtrack_grid(grid: List[List[str]], r: int, c: int) -> None:
    """In-place mark visited, recurse 4-dir, unmark (if the cell can be reused)."""
    rows, cols = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return
    tmp, grid[r][c] = grid[r][c], "#"
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        backtrack_grid(grid, r + dr, c + dc)
    grid[r][c] = tmp


# ---------------------------------------------------------------------------
# 1-D DP
# ---------------------------------------------------------------------------

def dp_one_array(n: int) -> int:
    """Define dp[i], set base cases, iterate in dependency order."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # replace with the real recurrence
    return dp[n]


def dp_rolling(n: int) -> int:
    """When dp[i] only needs the last 1–2 states, drop the array."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ---------------------------------------------------------------------------
# Trie
# ---------------------------------------------------------------------------

class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
