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
# O(1) avg lookup / insert / delete. Use for frequency, grouping, membership
# ("have I seen this?"), and complement lookups. A set is a map with no values.

def frequency_map(items: List[int]) -> Dict[int, int]:
    """Count how many times each value appears.

    Classic grouping pattern: key = the item, value = its count.
    Also: ``Counter(items)`` or ``defaultdict(int)``.
    """
    counts: Dict[int, int] = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    return counts


def complement_lookup(nums: List[int], target: int) -> Optional[tuple[int, int]]:
    """Return indices of two numbers that add up to ``target``, or None.

    For each ``x``, look up ``target - x`` in a seen map of value -> index
    (Two Sum). Record ``x`` after the lookup so a number is not paired with itself.
    """
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
# Two indices walk an array in O(n). Opposite ends for sorted pairs / palindromes;
# same direction (slow/fast) for in-place filter, remove-duplicates, or a midpoint.

def two_pointers_opposite(arr: List[int]) -> None:
    """Walk a sorted array from both ends toward a valid pair.

    Move the pointer that can improve the current pair: too small → ``l += 1``,
    too large → ``r -= 1``. Record on a hit, then advance one or both.
    """
    l, r = 0, len(arr) - 1
    while l < r:
        # if too small: l += 1
        # if too large: r -= 1
        # if equal / valid: record, then l += 1 and/or r -= 1
        l += 1  # placeholder so the skeleton runs


def two_pointers_same_direction(arr: List[int]) -> None:
    """Slow trails, fast scans: in-place keep / overwrite.

    Fast reads every element; slow writes only the ones that should stay
    (remove duplicates, partition, compact). After the loop, ``slow`` is the new length.
    """
    slow = 0
    for fast in range(len(arr)):
        # if arr[fast] should be kept: arr[slow] = arr[fast]; slow += 1
        _ = fast
        _ = slow


# ---------------------------------------------------------------------------
# Stack
# ---------------------------------------------------------------------------
# LIFO. Use for matching (brackets, nested structure), undo, and "next greater /
# previous smaller" via a monotonic stack of indices.

def stack_matching(s: str) -> bool:
    """Return whether ``s`` has valid matching brackets.

    Push openers. On a closer, pop if it matches the top; otherwise invalid.
    Empty stack at the end means every opener was closed.
    """
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
    """Next greater element to the right for each index; ``-1`` if none.

    Keep an increasing stack of indices. When a new value is larger than the
    top, that top's "next greater" is the new value — pop until the stack is
    still increasing, then push.
    """
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
# FIFO. BFS, level-order, and sliding-window queues. Use ``deque`` so both
# ends are O(1) — never ``list.pop(0)``.

def bfs_queue(start: int, adj: Dict[int, List[int]]) -> List[int]:
    """Level-order walk from ``start``; return visit order.

    Mark a node seen when it is *enqueued*, not when it is popped, so it is
    not added twice. ``popleft`` is O(1); ``list.pop(0)`` is O(n).
    """
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
# Sequential nodes, O(1) extra space. Reverse by rewiring pointers; dummy head
# for insert/delete at the real head; slow/fast for midpoint or cycle.

class ListNode:
    """Singly linked list node: ``val`` and ``next``."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a list in place; return the new head (old tail).

    Three pointers: ``prev``, ``curr``, ``nxt``. Save ``nxt``, point ``curr``
    backward at ``prev``, then slide all three forward.
    """
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def dummy_head_pattern(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the real head after operating from a dummy node.

    A dummy in front of ``head`` makes insert/delete at the first real node
    the same as anywhere else — no special-case for ``head`` itself.
    """
    dummy = ListNode(0, head)
    _ = dummy.next  # operate from dummy
    return dummy.next


def slow_fast(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the midpoint (or meeting node if used for cycle detection).

    Fast moves two steps, slow moves one. When fast hits the end, slow is at
    the middle. If they ever meet before the end, there is a cycle.
    """
    slow = fast = head
    while fast and fast.next:
        assert slow is not None
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_two_sorted(
    a: Optional[ListNode], b: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted lists into one sorted list; return the new head.

    Dummy + tail: always append the smaller of ``a`` / ``b``, then attach
    whatever remains. Dummy avoids a special case for the first node.
    """
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
# Hierarchy: paths, LCA, BST property. DFS (recurse or stack) for depth / paths;
# BFS (queue) for level order and "closest to root".

class TreeNode:
    """Binary tree node: ``val``, ``left``, ``right``."""

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
    """Walk the tree with recursion (pre/in/post: move the visit line).

    Base case: ``None``. This skeleton is post-order (children then node);
    visit before both recursions for pre-order, between them for in-order.
    """
    if not root:
        return
    dfs_recursive(root.left)
    dfs_recursive(root.right)


def dfs_iterative(root: Optional[TreeNode]) -> List[int]:
    """Pre-order walk with an explicit stack; return visit order.

    Pop, visit, then push right *then* left so left is processed first.
    Same idea as recursion, without the call stack.
    """
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
    """Level-order traversal: one inner list per depth.

    Snapshot ``len(q)`` as the current level's size, then drain that many
    nodes and enqueue their children for the next level.
    """
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
# Nodes + edges. BFS for unweighted shortest path / components; DFS for
# reachability and cycles; Kahn / 3-color DFS when ordering has prerequisites.

def build_adj(n: int, edges: List[List[int]], directed: bool = False) -> List[List[int]]:
    """Build an adjacency list of size ``n`` from ``[u, v]`` edge pairs.

    Undirected edges are stored both ways. Nodes are assumed ``0 .. n-1``.
    """
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def graph_dfs(n: int, adj: List[List[int]]) -> List[int]:
    """DFS every component; return visit order.

    Outer loop covers disconnected graphs. Mark visited on entry so a node
    is not re-entered through another edge.
    """
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
    """Return True if the directed graph has a cycle (3-color DFS).

    ``0`` unvisited, ``1`` visiting (on the recursion stack), ``2`` done.
    Seeing a neighbor still in state 1 means a back edge — a cycle.
    """
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
    """Topological order via BFS on indegree; ``None`` if there is a cycle.

    Start with all indegree-0 nodes. Each processed node decrements its
    neighbors; a neighbor with indegree 0 is ready. If fewer than ``n``
    nodes are emitted, a cycle remains.
    """
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
# Halve a sorted range in O(log n). Exact match on a sorted array, or search
# the answer: first / last index (or value) where a monotonic predicate is True.

def binary_search_exact(arr: List[int], target: int) -> int:
    """Return the index of ``target`` in a sorted array, or ``-1``.

    Inclusive ``[l, r]``. Mid too small → search right (``l = mid + 1``);
    mid too large → search left (``r = mid - 1``).
    """
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
    """Smallest ``x`` in ``[lo, hi]`` where ``predicate(x)`` is True.

    ``hi`` is inclusive. The predicate must be monotonic (False then True).
    Caller must guarantee a True exists, or check ``predicate(lo)`` after.
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
# Subarray / substring of a stream. Expand the right end; shrink the left while
# the window is invalid. Typical O(n) because each index enters and leaves once.

def variable_window(s: str) -> int:
    """Longest valid window length (skeleton — replace the invalid check).

    Grow ``r`` each step, update counts, then shrink ``l`` while the window
    breaks the constraint. ``r - l + 1`` is the current length.
    """
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
# Priority queue: kth / top-k / running median. ``heapq`` is a min-heap;
# negate values for a max-heap. Push/pop are O(log n); peek min is O(1).

def top_k_min_heap(nums: List[int], k: int) -> List[int]:
    """Return the ``k`` largest values (unordered) using a min-heap of size ``k``.

    Anything smaller than the current heap min cannot be in the top k, so it
    is ignored. ``heapreplace`` pops the min and pushes the new value in one step.
    """
    heap: List[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap


def max_heap_push(heap: List[int], x: int) -> None:
    """Push ``x`` onto a max-heap stored as negated values.

    ``heapq`` only implements a min-heap, so store ``-x``. Pair with
    ``max_heap_pop``.
    """
    heapq.heappush(heap, -x)


def max_heap_pop(heap: List[int]) -> int:
    """Pop and return the true max from a negated min-heap."""
    return -heapq.heappop(heap)


# ---------------------------------------------------------------------------
# Backtracking
# ---------------------------------------------------------------------------
# Explore all combinations / permutations / paths. Choose, recurse, undo
# (pop / unmark). Prune as soon as a partial path cannot succeed.

def backtrack_subsets(nums: List[int]) -> List[List[int]]:
    """All subsets of ``nums`` (include / skip at each index).

    At index ``i``: append ``nums[i]`` and recurse, then pop and recurse
    without it. Copy ``path`` when you reach the end — it is reused.
    """
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
    """DFS a grid in 4 directions, marking the cell visited then unmarking.

    In-place ``"#"`` (or similar) so the same cell is not reused on this path.
    Restore after the four recursive calls if the cell can be used on another path.
    """
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
# Min/max over overlapping subproblems. Define ``dp[i]``, set base cases, fill
# in dependency order. If only the last 1–2 states are needed, roll variables.

def dp_one_array(n: int) -> int:
    """Fill ``dp[0..n]`` from base cases using a recurrence (Fibonacci skeleton).

    ``dp[i]`` = answer for size ``i``. Iterate ``i`` so that ``i-1``, ``i-2``,
    … are already computed. Replace the recurrence with the problem's.
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # replace with the real recurrence
    return dp[n]


def dp_rolling(n: int) -> int:
    """Same recurrence as ``dp_one_array``, using only the last two states.

    When ``dp[i]`` depends only on ``dp[i-1]`` and ``dp[i-2]``, two variables
    replace the array: O(1) extra space.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ---------------------------------------------------------------------------
# Trie
# ---------------------------------------------------------------------------
# Prefix tree: one edge per character. Insert / search / prefix in O(L) where
# L is the word length. Use for dictionaries, autocomplete, and wildcard search.

class TrieNode:
    """One character in the trie: child map and an end-of-word flag."""

    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_word = False


class Trie:
    """Rooted prefix tree. Keys are strings; nodes are shared prefixes."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Add ``word``. Create missing child nodes; mark the last as a word."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        """Return True iff ``word`` was inserted (not merely a prefix)."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        """Return True iff some inserted word starts with ``prefix``."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
