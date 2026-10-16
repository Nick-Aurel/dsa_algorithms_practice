"""
DSA interview templates (Python 3).

Write these from memory during Hour 0. If you cannot reproduce a snippet
without looking, you cannot use it under interview pressure.

These are skeletons — not problem solutions. Fill in / re-type, then start Blind 75.

13 concepts, numbered below.
"""

# Let annotations name classes that are defined later in this file.
from __future__ import annotations

# Min-heap push, pop, and replace.
import heapq
# Counter for frequencies, defaultdict for missing keys, deque for O(1) ends.
from collections import Counter, defaultdict, deque
# Names used in the function signatures below.
from typing import Dict, List, Optional, Set


# ---------------------------------------------------------------------------
# 1) Hash map / set
# ---------------------------------------------------------------------------
# A hash map is a set of labeled drawers. You store something under a name
# (the key) and later open that exact drawer, instead of searching every one.
# A set is the same idea with no extra payload: only "is this thing in here?"
#
# Real life: a coat check. You get a ticket number; they hand you that coat
# without looking through the rack. A guest list at the door is a set —
# your name is either on it or it isn't.
#
# O(1) avg lookup / insert / delete. Use for frequency, grouping, membership
# ("have I seen this?"), and complement lookups. A set is a map with no values.

def frequency_map(items: List[int]) -> Dict[int, int]:
    """Count how many times each value appears.

    Classic grouping pattern: key = the item, value = its count.
    Also: ``Counter(items)`` or ``defaultdict(int)``.
    """
    # Start with no counts recorded.
    counts: Dict[int, int] = {}
    # Look at each item once.
    for x in items:
        # Add one to this value's count; a missing key counts as zero.
        counts[x] = counts.get(x, 0) + 1
    # value -> how many times it appeared.
    return counts


def complement_lookup(nums: List[int], target: int) -> Optional[tuple[int, int]]:
    """Return indices of two numbers that add up to ``target``, or None.

    For each ``x``, look up ``target - x`` in a seen map of value -> index
    (Two Sum). Record ``x`` after the lookup so a number is not paired with itself.
    """
    # value -> index of a number already passed.
    seen: Dict[int, int] = {}
    # Walk left to right, keeping each number's index.
    for i, x in enumerate(nums):
        # The other number that would complete the pair.
        need = target - x
        # The complement was seen earlier: those two indices are the answer.
        if need in seen:
            return seen[need], i
        # Record this number after the lookup so it is not paired with itself.
        seen[x] = i
    # No pair added up to the target.
    return None


# ---------------------------------------------------------------------------
# 2) Two pointers
# ---------------------------------------------------------------------------
# Two fingers walking a line of items. Sometimes they start at opposite ends
# and move toward each other. Sometimes one stays slow while the other scans
# ahead and only the slow finger writes down what should stay.
#
# Real life: a height-sorted line, looking for two people whose heights add
# to a target. Start with the shortest and the tallest. Too short? Step the
# short end inward. Too tall? Step the tall end inward.
#
# Two indices walk an array in O(n). Opposite ends for sorted pairs / palindromes;
# same direction (slow/fast) for in-place filter, remove-duplicates, or a midpoint.

def two_pointers_opposite(arr: List[int]) -> None:
    """Walk a sorted array from both ends toward a valid pair.

    Move the pointer that can improve the current pair: too small → ``l += 1``,
    too large → ``r -= 1``. Record on a hit, then advance one or both.
    """
    # Left starts at the small end; right starts at the large end.
    l, r = 0, len(arr) - 1
    # Stop once the two ends meet or cross.
    while l < r:
        # if too small: l += 1
        # if too large: r -= 1
        # if equal / valid: record, then l += 1 and/or r -= 1
        # Placeholder step so the skeleton ends; replace with the real move.
        l += 1


def two_pointers_same_direction(arr: List[int]) -> None:
    """Slow trails, fast scans: in-place keep / overwrite.

    Fast reads every element; slow writes only the ones that should stay
    (remove duplicates, partition, compact). After the loop, ``slow`` is the new length.
    """
    # Next slot to write a kept value. It advances only when something stays.
    slow = 0
    # fast reads every index from left to right.
    for fast in range(len(arr)):
        # if arr[fast] should be kept: arr[slow] = arr[fast]; slow += 1
        # Placeholder reads so the skeleton runs; replace with the keep/write step.
        _ = fast
        _ = slow


# ---------------------------------------------------------------------------
# 3) Stack
# ---------------------------------------------------------------------------
# A stack of plates. You add and remove only from the top, so the last thing
# you put on is the first thing you take off.
#
# Real life: undo. Each action is a plate; undo lifts the most recent one.
# Nested boxes work the same way: the last box you opened is the next one
# you must close.
#
# LIFO. Use for matching (brackets, nested structure), undo, and "next greater /
# previous smaller" via a monotonic stack of indices.

def stack_matching(s: str) -> bool:
    """Return whether ``s`` has valid matching brackets.

    Push openers. On a closer, pop if it matches the top; otherwise invalid.
    Empty stack at the end means every opener was closed.
    """
    # Each closer maps to the opener it must match.
    pairs = {")": "(", "]": "[", "}": "{"}
    # Openers still waiting, most recent on top.
    st: List[str] = []
    # Check one character at a time.
    for ch in s:
        # This character is a closer.
        if ch in pairs:
            # Nothing to close, or the top opener is the wrong kind.
            if not st or st[-1] != pairs[ch]:
                return False
            # Matched: remove that opener.
            st.pop()
        else:
            # An opener waits until its closer shows up.
            st.append(ch)
    # Valid only when every opener was closed.
    return not st


def monotonic_stack(arr: List[int]) -> List[int]:
    """Next greater element to the right for each index; ``-1`` if none.

    Keep an increasing stack of indices. When a new value is larger than the
    top, that top's "next greater" is the new value — pop until the stack is
    still increasing, then push.
    """
    # One answer per index.
    n = len(arr)
    # Default: nothing greater sits to the right.
    ans = [-1] * n
    # Indices still waiting for a greater value, smallest recent one on top.
    st: List[int] = []
    # Each new value may resolve indices still waiting on the stack.
    for i, x in enumerate(arr):
        # Pop every smaller index; this value is their next greater.
        while st and arr[st[-1]] < x:
            ans[st.pop()] = x
        # This index now waits for something larger on its right.
        st.append(i)
    return ans


# ---------------------------------------------------------------------------
# 4) Queue / deque
# ---------------------------------------------------------------------------
# A line at a counter. The first person who joins is the first person served.
# A deque is that line with a second door at the back, so you can also add
# or remove from the end in one step.
#
# Real life: a deli. You take a number and wait. People are helped in the
# order they arrived, not by who happens to be standing closest.
#
# FIFO. BFS, level-order, and sliding-window queues. Use ``deque`` so both
# ends are O(1) — never ``list.pop(0)``.

def bfs_queue(start: int, adj: Dict[int, List[int]]) -> List[int]:
    """Level-order walk from ``start``; return visit order.

    Mark a node seen when it is *enqueued*, not when it is popped, so it is
    not added twice. ``popleft`` is O(1); ``list.pop(0)`` is O(n).
    """
    # The line starts with the source.
    q: deque[int] = deque([start])
    # Mark seen when enqueued so the same node is not added twice.
    seen: Set[int] = {start}
    # Filled in the order nodes are served.
    order: List[int] = []
    # Keep going while someone is still waiting.
    while q:
        # Serve whoever has been waiting the longest.
        node = q.popleft()
        order.append(node)
        # Each neighbor is one step farther from the source.
        for nei in adj.get(node, []):
            # Skip nodes already in line or already visited.
            if nei not in seen:
                seen.add(nei)
                # New neighbors wait behind everyone already queued.
                q.append(nei)
    return order


# ---------------------------------------------------------------------------
# 5) Linked list
# ---------------------------------------------------------------------------
# A chain of people holding hands. Each person knows only who comes next,
# not the whole line, so reaching the middle means walking from the front.
# You can reverse the chain by having each person let go and grab the one
# behind them.
#
# Real life: a scavenger hunt. Each clue only says where the next clue is.
# You cannot jump to clue 5; you follow the chain.
#
# Sequential nodes, O(1) extra space. Reverse by rewiring pointers; dummy head
# for insert/delete at the real head; slow/fast for midpoint or cycle.

class ListNode:
    """Singly linked list node: ``val`` and ``next``."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        # This node's payload.
        self.val = val
        # The following node, or None at the tail.
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a list in place; return the new head (old tail).

    Three pointers: ``prev``, ``curr``, ``nxt``. Save ``nxt``, point ``curr``
    backward at ``prev``, then slide all three forward.
    """
    # Nothing is reversed yet; start walking at the original head.
    prev, curr = None, head
    # Stop once we have walked off the end of the list.
    while curr:
        # Save the rest of the list before this link is overwritten.
        nxt = curr.next
        # Point this node backward at the already-reversed part.
        curr.next = prev
        # This node is now the front of the reversed part.
        prev = curr
        # Step into the part that has not been reversed yet.
        curr = nxt
    # prev sits on the old tail, which is the new head.
    return prev


def dummy_head_pattern(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the real head after operating from a dummy node.

    A dummy in front of ``head`` makes insert/delete at the first real node
    the same as anywhere else — no special-case for ``head`` itself.
    """
    # A fake node in front, so the real head is not a special case.
    dummy = ListNode(0, head)
    # The first real node. Do the insert or delete from here.
    _ = dummy.next
    # Skip the fake node and hand back the real head.
    return dummy.next


def slow_fast(head: Optional[ListNode]) -> Optional[ListNode]:
    """Return the midpoint (or meeting node if used for cycle detection).

    Fast moves two steps, slow moves one. When fast hits the end, slow is at
    the middle. If they ever meet before the end, there is a cycle.
    """
    # Both start together; fast will pull ahead.
    slow = fast = head
    # Stop when fast cannot take two more steps.
    while fast and fast.next:
        # slow still points at a node while fast has somewhere to step.
        assert slow is not None
        # One step.
        slow = slow.next
        # Two steps.
        fast = fast.next.next
    # Middle of the list, or the meeting node in a cycle check.
    return slow


def merge_two_sorted(
    a: Optional[ListNode], b: Optional[ListNode]
) -> Optional[ListNode]:
    """Merge two sorted lists into one sorted list; return the new head.

    Dummy + tail: always append the smaller of ``a`` / ``b``, then attach
    whatever remains. Dummy avoids a special case for the first node.
    """
    # Fake head so the first real node attaches like any later one.
    dummy = ListNode()
    # Last node of the merged list so far.
    tail = dummy
    # Keep taking from both lists while both still have nodes.
    while a and b:
        # a is smaller or tied: append it and advance a.
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            # b is smaller: append it and advance b.
            tail.next, b = b, b.next
        # The node just appended is the new end.
        tail = tail.next
    # The leftover list is already sorted; attach it in one link.
    tail.next = a or b
    # Skip the fake head.
    return dummy.next


# ---------------------------------------------------------------------------
# 6) Binary tree DFS / BFS
# ---------------------------------------------------------------------------
# A family tree where each person has at most two children, left and right.
# Depth-first finishes one whole branch before starting the other. Breadth-
# first visits everyone in the same generation before going a level deeper.
#
# Real life: an org chart, or a choose-your-own-adventure book where each
# page offers two choices. "Who is closest to the boss?" is breadth-first.
# "Follow this branch all the way down" is depth-first.
#
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
        # This node's payload.
        self.val = val
        # Left child, or None.
        self.left = left
        # Right child, or None.
        self.right = right


def dfs_recursive(root: Optional[TreeNode]) -> None:
    """Walk the tree with recursion (pre/in/post: move the visit line).

    Base case: ``None``. This skeleton is post-order (children then node);
    visit before both recursions for pre-order, between them for in-order.
    """
    # Empty child: this branch is finished.
    if not root:
        return
    # Finish the whole left branch first.
    dfs_recursive(root.left)
    # Then finish the whole right branch. Visit the node here for post-order.
    dfs_recursive(root.right)


def dfs_iterative(root: Optional[TreeNode]) -> List[int]:
    """Pre-order walk with an explicit stack; return visit order.

    Pop, visit, then push right *then* left so left is processed first.
    Same idea as recursion, without the call stack.
    """
    # Nothing to visit.
    if not root:
        return []
    # Stands in for the call stack. Root is visited first.
    st: List[TreeNode] = [root]
    # Pre-order: record a node when it is popped.
    order: List[int] = []
    # Continue while nodes are still waiting.
    while st:
        # Most recently pushed node comes off first.
        node = st.pop()
        order.append(node.val)
        # Push right before left so left is processed next.
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
    # Empty tree has no levels.
    if not root:
        return []
    # Level 0 is just the root.
    q: deque[TreeNode] = deque([root])
    # One inner list per depth.
    levels: List[List[int]] = []
    # Each pass of the outer loop is one depth.
    while q:
        # Values at this depth.
        level: List[int] = []
        # Freeze the size so children enqueued now wait for the next level.
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            # Left child joins the next level, if it exists.
            if node.left:
                q.append(node.left)
            # Right child joins the next level, if it exists.
            if node.right:
                q.append(node.right)
        levels.append(level)
    return levels


# ---------------------------------------------------------------------------
# 7) Graph: adj list, DFS, BFS, Kahn topo
# ---------------------------------------------------------------------------
# A map of places and the roads between them. Places are nodes; roads are
# edges. Depth-first wanders down one road as far as it goes. Breadth-first
# checks every place one stop away before going farther. If some roads are
# one-way and a task cannot start until others finish, you begin with
# whatever nothing is blocking.
#
# Real life: a subway map. "Fewest stops from here" is breadth-first. A
# course plan where Calculus 2 requires Calculus 1 is the same picture:
# take the class that has no unfinished prerequisite.
#
# Nodes + edges. BFS for unweighted shortest path / components; DFS for
# reachability and cycles; Kahn / 3-color DFS when ordering has prerequisites.

def build_adj(n: int, edges: List[List[int]], directed: bool = False) -> List[List[int]]:
    """Build an adjacency list of size ``n`` from ``[u, v]`` edge pairs.

    Undirected edges are stored both ways. Nodes are assumed ``0 .. n-1``.
    """
    # One empty neighbor list per node, indices 0 .. n-1.
    adj: List[List[int]] = [[] for _ in range(n)]
    # Each pair is one road.
    for u, v in edges:
        # u can step to v.
        adj[u].append(v)
        # An undirected road is stored in both directions.
        if not directed:
            adj[v].append(u)
    return adj


def graph_dfs(n: int, adj: List[List[int]]) -> List[int]:
    """DFS every component; return visit order.

    Outer loop covers disconnected graphs. Mark visited on entry so a node
    is not re-entered through another edge.
    """
    # False until this node is entered.
    seen = [False] * n
    # Visit order across every component.
    order: List[int] = []

    def dfs(u: int) -> None:
        # Mark on entry so another edge cannot re-enter this node.
        seen[u] = True
        order.append(u)
        # Follow each outgoing road.
        for v in adj[u]:
            # Skip nodes already on some path.
            if not seen[v]:
                dfs(v)

    # A new start reaches nodes that no earlier component touched.
    for u in range(n):
        if not seen[u]:
            dfs(u)
    return order


def has_cycle_directed(n: int, adj: List[List[int]]) -> bool:
    """Return True if the directed graph has a cycle (3-color DFS).

    ``0`` unvisited, ``1`` visiting (on the recursion stack), ``2`` done.
    Seeing a neighbor still in state 1 means a back edge — a cycle.
    """
    # 0 unseen, 1 on the current path, 2 finished.
    state = [0] * n

    def dfs(u: int) -> bool:
        # Put this node on the current path.
        state[u] = 1
        for v in adj[u]:
            # A neighbor still on this path is a back edge: a cycle.
            if state[v] == 1:
                return True
            # Explore an unseen neighbor and stop as soon as a cycle appears.
            if state[v] == 0 and dfs(v):
                return True
        # This node and everything below it are finished.
        state[u] = 2
        return False

    # Try every unseen start. Any cycle makes the whole answer True.
    return any(state[u] == 0 and dfs(u) for u in range(n))


def kahn_topo(n: int, adj: List[List[int]]) -> Optional[List[int]]:
    """Topological order via BFS on indegree; ``None`` if there is a cycle.

    Start with all indegree-0 nodes. Each processed node decrements its
    neighbors; a neighbor with indegree 0 is ready. If fewer than ``n``
    nodes are emitted, a cycle remains.
    """
    # How many unfinished prerequisites each node still has.
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            # Edge u -> v is one prerequisite of v.
            indeg[v] += 1
    # Nodes nothing is blocking can go first.
    q: deque[int] = deque([u for u in range(n) if indeg[u] == 0])
    # A valid order, built as nodes become ready.
    order: List[int] = []
    while q:
        # Take a node whose prerequisites are all done.
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            # u is finished, so v has one fewer blocker.
            indeg[v] -= 1
            # v is ready once nothing is left in front of it.
            if indeg[v] == 0:
                q.append(v)
    # Fewer than n nodes means a cycle left some nodes blocked forever.
    return order if len(order) == n else None


# ---------------------------------------------------------------------------
# 8) Binary search
# ---------------------------------------------------------------------------
# A guessing game on a sorted list. Each guess throws away half of what is
# left, so you reach the answer in a handful of tries instead of checking
# every item.
#
# Real life: finding a word in a dictionary. Open the middle. If your word
# comes later, ignore the left half and repeat on the right.
#
# Halve a sorted range in O(log n). Exact match on a sorted array, or search
# the answer: first / last index (or value) where a monotonic predicate is True.

def binary_search_exact(arr: List[int], target: int) -> int:
    """Return the index of ``target`` in a sorted array, or ``-1``.

    Inclusive ``[l, r]``. Mid too small → search right (``l = mid + 1``);
    mid too large → search left (``r = mid - 1``).
    """
    # Search the whole array; both ends are included.
    l, r = 0, len(arr) - 1
    # An empty range means the target is absent.
    while l <= r:
        # Middle of what is still in play.
        mid = (l + r) // 2
        # Found it.
        if arr[mid] == target:
            return mid
        # Target lives strictly to the right of mid.
        if arr[mid] < target:
            l = mid + 1
        else:
            # Target lives strictly to the left of mid.
            r = mid - 1
    return -1


def binary_search_first_true(lo: int, hi: int, predicate) -> int:
    """Smallest ``x`` in ``[lo, hi]`` where ``predicate(x)`` is True.

    ``hi`` is inclusive. The predicate must be monotonic (False then True).
    Caller must guarantee a True exists, or check ``predicate(lo)`` after.
    """
    # Shrink until lo and hi name the same index.
    while lo < hi:
        mid = (lo + hi) // 2
        # True here, so the first True is mid or somewhere to its left.
        if predicate(mid):
            hi = mid
        else:
            # Still False, so the first True is strictly to the right.
            lo = mid + 1
    return lo


# ---------------------------------------------------------------------------
# 9) Sliding window
# ---------------------------------------------------------------------------
# A moving frame over a row of items. Grow it from the right. When the group
# inside breaks the rule, shrink it from the left until the rule holds again.
# Each item enters the frame once and leaves once.
#
# Real life: a tour bus with a seat limit driving along a line of people.
# People board at the front of the group. When the bus is over the limit,
# people at the back of the group step off until it fits.
#
# Subarray / substring of a stream. Expand the right end; shrink the left while
# the window is invalid. Typical O(n) because each index enters and leaves once.

def variable_window(s: str) -> int:
    """Longest valid window length (skeleton — replace the invalid check).

    Grow ``r`` each step, update counts, then shrink ``l`` while the window
    breaks the constraint. ``r - l + 1`` is the current length.
    """
    # How many times each character sits inside the window.
    counts: Dict[str, int] = defaultdict(int)
    # Left edge of the window.
    l = 0
    # Best valid length seen so far.
    best = 0
    # Right edge grows by one character each step.
    for r, ch in enumerate(s):
        # The new right-edge character enters the window.
        counts[ch] += 1
        # Replace False with the real "window is invalid" check, then shrink.
        while False:
            # The character at the left edge leaves the window.
            counts[s[l]] -= 1
            # Slide the left edge forward.
            l += 1
        # Current window length is a candidate.
        best = max(best, r - l + 1)
    return best


# ---------------------------------------------------------------------------
# 10) Heap
# ---------------------------------------------------------------------------
# A pile that always lets you grab the smallest item quickly, even while new
# items keep arriving. To grab the largest instead, store the numbers flipped
# (negative), so the "smallest" stored value is really the biggest one.
#
# Real life: an emergency room. Patients are not seen in arrival order. The
# most urgent person is always next, and a new arrival can jump the line.
#
# Priority queue: kth / top-k / running median. ``heapq`` is a min-heap;
# negate values for a max-heap. Push/pop are O(log n); peek min is O(1).

def top_k_min_heap(nums: List[int], k: int) -> List[int]:
    """Return the ``k`` largest values (unordered) using a min-heap of size ``k``.

    Anything smaller than the current heap min cannot be in the top k, so it
    is ignored. ``heapreplace`` pops the min and pushes the new value in one step.
    """
    # The k largest values seen so far. The smallest of them sits at heap[0].
    heap: List[int] = []
    for x in nums:
        # Heap is not full yet, so every value is still a candidate.
        if len(heap) < k:
            heapq.heappush(heap, x)
        # Bigger than the smallest of the current top k, so it belongs.
        elif x > heap[0]:
            # Drop that smallest value and insert x in one step.
            heapq.heapreplace(heap, x)
    return heap


def max_heap_push(heap: List[int], x: int) -> None:
    """Push ``x`` onto a max-heap stored as negated values.

    ``heapq`` only implements a min-heap, so store ``-x``. Pair with
    ``max_heap_pop``.
    """
    # Negate so the smallest stored value is the true maximum.
    heapq.heappush(heap, -x)


def max_heap_pop(heap: List[int]) -> int:
    """Pop and return the true max from a negated min-heap."""
    # Undo the negation to hand back the real maximum.
    return -heapq.heappop(heap)


# ---------------------------------------------------------------------------
# 11) Backtracking
# ---------------------------------------------------------------------------
# Try a choice, go further, and if that path fails, undo the choice and try
# the next one. Stop early when a partial attempt already cannot succeed.
#
# Real life: trying on outfits. Pick a shirt, then pants. If they clash, put
# the pants back and try another pair. If nothing works with that shirt, put
# the shirt back too and start over with a different one.
#
# Explore all combinations / permutations / paths. Choose, recurse, undo
# (pop / unmark). Prune as soon as a partial path cannot succeed.

def backtrack_subsets(nums: List[int]) -> List[List[int]]:
    """All subsets of ``nums`` (include / skip at each index).

    At index ``i``: append ``nums[i]`` and recurse, then pop and recurse
    without it. Copy ``path`` when you reach the end — it is reused.
    """
    # Every finished subset.
    ans: List[List[int]] = []
    # The subset being built. It is reused across branches.
    path: List[int] = []

    def dfs(i: int) -> None:
        # Every index has been decided. Copy path because it will be mutated.
        if i == len(nums):
            ans.append(path[:])
            return
        # Choice 1: include nums[i], then decide the rest.
        path.append(nums[i])
        dfs(i + 1)
        # Undo that include before trying the other branch.
        path.pop()
        # Choice 2: skip nums[i].
        dfs(i + 1)

    # Start the include/skip decisions at index 0.
    dfs(0)
    return ans


def backtrack_grid(grid: List[List[str]], r: int, c: int) -> None:
    """DFS a grid in 4 directions, marking the cell visited then unmarking.

    In-place ``"#"`` (or similar) so the same cell is not reused on this path.
    Restore after the four recursive calls if the cell can be used on another path.
    """
    # Grid bounds, used by the guard below.
    rows, cols = len(grid), len(grid[0])
    # This step walked off the grid.
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return
    # Remember the real character, then mark the cell used on this path.
    tmp, grid[r][c] = grid[r][c], "#"
    # Try down, up, right, and left.
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        backtrack_grid(grid, r + dr, c + dc)
    # Put the character back so a different path can use this cell.
    grid[r][c] = tmp


# ---------------------------------------------------------------------------
# 12) 1-D DP
# ---------------------------------------------------------------------------
# Solve a big problem by writing down the answers to the smaller versions of
# the same problem, in order, so you never redo work you already finished.
#
# Real life: climbing stairs one or two steps at a time. The ways to reach
# step 10 are the ways to reach step 9 plus the ways to reach step 8. You
# remember those two numbers instead of recounting from the bottom.
#
# Min/max over overlapping subproblems. Define ``dp[i]``, set base cases, fill
# in dependency order. If only the last 1–2 states are needed, roll variables.

def dp_one_array(n: int) -> int:
    """Fill ``dp[0..n]`` from base cases using a recurrence (Fibonacci skeleton).

    ``dp[i]`` = answer for size ``i``. Iterate ``i`` so that ``i-1``, ``i-2``,
    … are already computed. Replace the recurrence with the problem's.
    """
    # The answer for size 0 or 1 is the size itself.
    if n <= 1:
        return n
    # One slot per size from 0 through n.
    dp = [0] * (n + 1)
    # Base cases the loop builds on.
    dp[0], dp[1] = 0, 1
    # i-1 and i-2 are already filled when i is computed.
    for i in range(2, n + 1):
        # Replace with the problem's recurrence.
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def dp_rolling(n: int) -> int:
    """Same recurrence as ``dp_one_array``, using only the last two states.

    When ``dp[i]`` depends only on ``dp[i-1]`` and ``dp[i-2]``, two variables
    replace the array: O(1) extra space.
    """
    # Same base cases as the array version.
    if n <= 1:
        return n
    # a is the state two steps back; b is the previous state.
    a, b = 0, 1
    # Each lap slides the window forward by one size.
    for _ in range(2, n + 1):
        # Old b becomes the new a; a + b is the new state.
        a, b = b, a + b
    # b holds the answer for size n.
    return b


# ---------------------------------------------------------------------------
# 13) Trie
# ---------------------------------------------------------------------------
# A tree of letters. Words that start the same way share the beginning of
# the path, so you walk one letter at a time instead of comparing a whole
# word against every word you know.
#
# Real life: phone contacts. You type "Sa" and it walks S, then a, then
# shows Sam, Sarah, and Samir — it does not reread every name from scratch.
#
# Prefix tree: one edge per character. Insert / search / prefix in O(L) where
# L is the word length. Use for dictionaries, autocomplete, and wildcard search.

class TrieNode:
    """One character in the trie: child map and an end-of-word flag."""

    def __init__(self) -> None:
        # Next letter -> child. A missing letter means that branch is absent.
        self.children: Dict[str, TrieNode] = {}
        # True only when an inserted word ends on this node.
        self.is_word = False


class Trie:
    """Rooted prefix tree. Keys are strings; nodes are shared prefixes."""

    def __init__(self) -> None:
        # Every word starts from this empty root.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Add ``word``. Create missing child nodes; mark the last as a word."""
        # Walk down from the root, one character per step.
        node = self.root
        for ch in word:
            # Open a new branch when this letter has not been seen here.
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # Step onto that letter.
            node = node.children[ch]
        # The walk ended on a complete word, not only a prefix.
        node.is_word = True

    def search(self, word: str) -> bool:
        """Return True iff ``word`` was inserted (not merely a prefix)."""
        node = self.root
        for ch in word:
            # A missing letter means this word was never inserted.
            if ch not in node.children:
                return False
            node = node.children[ch]
        # True only if a word ends here, not merely as a longer word's prefix.
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        """Return True iff some inserted word starts with ``prefix``."""
        node = self.root
        for ch in prefix:
            # The prefix itself is missing, so no word can start with it.
            if ch not in node.children:
                return False
            node = node.children[ch]
        # Reaching the last letter means some word continues through here.
        return True
