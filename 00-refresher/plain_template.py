"""
DSA interview templates (Python).

Write these from memory during Hour 0. If you cannot reproduce a snippet
without looking, you cannot use it under interview pressure.

These are skeletons — not problem solutions. Fill in / re-type, then start Blind 75.

13 concepts, numbered below.
"""

import heapq
from collections import Counter, defaultdict, deque


# ---------------------------------------------------------------------------
# 1) Hash map / set
# ---------------------------------------------------------------------------
# Interview walkthrough for frequency_map — say this out loud, then write it.
#
# "I need how many times each value appears. A nested scan would re-search
# the whole list for every item, which is O(n^2). A hash map lets me open
# one labeled drawer in average O(1): the key is the value itself, and what
# I store in that drawer is the count so far.
#
# Start with an empty map. Nothing has been counted.
#
# Walk the list once. For the item in my hand:
#   1. Look it up. A missing key means I have seen it zero times.
#   2. Add one to that count.
#   3. Put the new count back in the same drawer.
#
# Worked example: items = [2, 1, 2, 3, 1, 2]
#   see 2 → {}              becomes {2: 1}
#   see 1 →                 {2: 1, 1: 1}
#   see 2 → 2 is already 1, store 2 → {2: 2, 1: 1}
#   see 3 →                 {2: 2, 1: 1, 3: 1}
#   see 1 → 1 is already 1, store 2 → {2: 2, 1: 2, 3: 1}
#   see 2 → 2 is already 2, store 3 → {2: 3, 1: 2, 3: 1}
#
# Hand that map back. 'How many 2s?' is one lookup, and the answer is 3.
#
# Time:  O(n). One pass, and each lookup or write is O(1) average.
# Space: O(k), where k is the number of distinct values. O(n) if all unique.
#
# counts.get(x, 0) is the whole trick. The 0 is only used the first time
# that value shows up. Every later visit reads the count already stored
# and writes count + 1."

def frequency_map(items):
    """Count how many times each value appears.

    Classic grouping pattern: key = the item, value = its count.
    Also: ``Counter(items)`` or ``defaultdict(int)``.
    """
    # Empty map: no value has been seen yet.
    counts = {}
    # One pass. Each item updates only its own drawer.
    for x in items:
        # Missing key → 0. Then store one more than whatever was there.
        counts[x] = counts.get(x, 0) + 1
    # value → how many times it appeared.
    return counts


def complement_lookup(nums, target):
    """Return indices of two numbers that add up to ``target``, or None.

    For each ``x``, look up ``target - x`` in a seen map of value -> index
    (Two Sum). Record ``x`` after the lookup so a number is not paired with itself.
    """
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    return None


# ---------------------------------------------------------------------------
# 2) Two pointers
# ---------------------------------------------------------------------------

def two_pointers_opposite(arr):
    """Walk a sorted array from both ends toward a valid pair.

    Move the pointer that can improve the current pair: too small → ``l += 1``,
    too large → ``r -= 1``. Record on a hit, then advance one or both.
    """
    l, r = 0, len(arr) - 1
    while l < r:
        l += 1


def two_pointers_same_direction(arr):
    """Slow trails, fast scans: in-place keep / overwrite.

    Fast reads every element; slow writes only the ones that should stay
    (remove duplicates, partition, compact). After the loop, ``slow`` is the new length.
    """
    slow = 0
    for fast in range(len(arr)):
        _ = fast
        _ = slow


# ---------------------------------------------------------------------------
# 3) Stack
# ---------------------------------------------------------------------------

def stack_matching(s):
    """Return whether ``s`` has valid matching brackets.

    Push openers. On a closer, pop if it matches the top; otherwise invalid.
    Empty stack at the end means every opener was closed.
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    st = []
    for ch in s:
        if ch in pairs:
            if not st or st[-1] != pairs[ch]:
                return False
            st.pop()
        else:
            st.append(ch)
    return not st


def monotonic_stack(arr):
    """Next greater element to the right for each index; ``-1`` if none.

    Keep an increasing stack of indices. When a new value is larger than the
    top, that top's "next greater" is the new value — pop until the stack is
    still increasing, then push.
    """
    n = len(arr)
    ans = [-1] * n
    st = []
    for i, x in enumerate(arr):
        while st and arr[st[-1]] < x:
            ans[st.pop()] = x
        st.append(i)
    return ans


# ---------------------------------------------------------------------------
# 4) Queue / deque
# ---------------------------------------------------------------------------

def bfs_queue(start, adj):
    """Level-order walk from ``start``; return visit order.

    Mark a node seen when it is *enqueued*, not when it is popped, so it is
    not added twice. ``popleft`` is O(1); ``list.pop(0)`` is O(n).
    """
    q = deque([start])
    seen = {start}
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj.get(node, []):
            if nei not in seen:
                seen.add(nei)
                q.append(nei)
    return order


# ---------------------------------------------------------------------------
# 5) Linked list
# ---------------------------------------------------------------------------

class ListNode:
    """Singly linked list node: ``val`` and ``next``."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
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


def dummy_head_pattern(head):
    """Return the real head after operating from a dummy node.

    A dummy in front of ``head`` makes insert/delete at the first real node
    the same as anywhere else — no special-case for ``head`` itself.
    """
    dummy = ListNode(0, head)
    _ = dummy.next
    return dummy.next


def slow_fast(head):
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


def merge_two_sorted(a, b):
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
# 6) Binary tree DFS / BFS
# ---------------------------------------------------------------------------

class TreeNode:
    """Binary tree node: ``val``, ``left``, ``right``."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_recursive(root):
    """Walk the tree with recursion (pre/in/post: move the visit line).

    Base case: ``None``. This skeleton is post-order (children then node);
    visit before both recursions for pre-order, between them for in-order.
    """
    if not root:
        return
    dfs_recursive(root.left)
    dfs_recursive(root.right)


def dfs_iterative(root):
    """Pre-order walk with an explicit stack; return visit order.

    Pop, visit, then push right *then* left so left is processed first.
    Same idea as recursion, without the call stack.
    """
    if not root:
        return []
    st = [root]
    order = []
    while st:
        node = st.pop()
        order.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return order


def bfs_levels(root):
    """Level-order traversal: one inner list per depth.

    Snapshot ``len(q)`` as the current level's size, then drain that many
    nodes and enqueue their children for the next level.
    """
    if not root:
        return []
    q = deque([root])
    levels = []
    while q:
        level = []
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
# 7) Graph: adj list, DFS, BFS, Kahn topo
# ---------------------------------------------------------------------------

def build_adj(n, edges, directed=False):
    """Build an adjacency list of size ``n`` from ``[u, v]`` edge pairs.

    Undirected edges are stored both ways. Nodes are assumed ``0 .. n-1``.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def graph_dfs(n, adj):
    """DFS every component; return visit order.

    Outer loop covers disconnected graphs. Mark visited on entry so a node
    is not re-entered through another edge.
    """
    seen = [False] * n
    order = []

    def dfs(u):
        seen[u] = True
        order.append(u)
        for v in adj[u]:
            if not seen[v]:
                dfs(v)

    for u in range(n):
        if not seen[u]:
            dfs(u)
    return order


def has_cycle_directed(n, adj):
    """Return True if the directed graph has a cycle (3-color DFS).

    ``0`` unvisited, ``1`` visiting (on the recursion stack), ``2`` done.
    Seeing a neighbor still in state 1 means a back edge — a cycle.
    """
    state = [0] * n

    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    return any(state[u] == 0 and dfs(u) for u in range(n))


def kahn_topo(n, adj):
    """Topological order via BFS on indegree; ``None`` if there is a cycle.

    Start with all indegree-0 nodes. Each processed node decrements its
    neighbors; a neighbor with indegree 0 is ready. If fewer than ``n``
    nodes are emitted, a cycle remains.
    """
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    q = deque([u for u in range(n) if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else None


# ---------------------------------------------------------------------------
# 8) Binary search
# ---------------------------------------------------------------------------

def binary_search_exact(arr, target):
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


def binary_search_first_true(lo, hi, predicate):
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
# 9) Sliding window
# ---------------------------------------------------------------------------

def variable_window(s):
    """Longest valid window length (skeleton — replace the invalid check).

    Grow ``r`` each step, update counts, then shrink ``l`` while the window
    breaks the constraint. ``r - l + 1`` is the current length.
    """
    counts = defaultdict(int)
    l = 0
    best = 0
    for r, ch in enumerate(s):
        counts[ch] += 1
        while False:
            counts[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best


# ---------------------------------------------------------------------------
# 10) Heap
# ---------------------------------------------------------------------------

def top_k_min_heap(nums, k):
    """Return the ``k`` largest values (unordered) using a min-heap of size ``k``.

    Anything smaller than the current heap min cannot be in the top k, so it
    is ignored. ``heapreplace`` pops the min and pushes the new value in one step.
    """
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap


def max_heap_push(heap, x):
    """Push ``x`` onto a max-heap stored as negated values.

    ``heapq`` only implements a min-heap, so store ``-x``. Pair with
    ``max_heap_pop``.
    """
    heapq.heappush(heap, -x)


def max_heap_pop(heap):
    """Pop and return the true max from a negated min-heap."""
    return -heapq.heappop(heap)


# ---------------------------------------------------------------------------
# 11) Backtracking
# ---------------------------------------------------------------------------

def backtrack_subsets(nums):
    """All subsets of ``nums`` (include / skip at each index).

    At index ``i``: append ``nums[i]`` and recurse, then pop and recurse
    without it. Copy ``path`` when you reach the end — it is reused.
    """
    ans = []
    path = []

    def dfs(i):
        if i == len(nums):
            ans.append(path[:])
            return
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
        dfs(i + 1)

    dfs(0)
    return ans


def backtrack_grid(grid, r, c):
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
# 12) 1-D DP
# ---------------------------------------------------------------------------

def dp_one_array(n):
    """Fill ``dp[0..n]`` from base cases using a recurrence (Fibonacci skeleton).

    ``dp[i]`` = answer for size ``i``. Iterate ``i`` so that ``i-1``, ``i-2``,
    … are already computed. Replace the recurrence with the problem's.
    """
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def dp_rolling(n):
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
# 13) Trie
# ---------------------------------------------------------------------------

class TrieNode:
    """One character in the trie: child map and an end-of-word flag."""

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """Rooted prefix tree. Keys are strings; nodes are shared prefixes."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Add ``word``. Create missing child nodes; mark the last as a word."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """Return True iff ``word`` was inserted (not merely a prefix)."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix):
        """Return True iff some inserted word starts with ``prefix``."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
