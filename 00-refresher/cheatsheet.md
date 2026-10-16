# Data structure cheatsheet (Python)

Hour 0: re-type the **13 concepts** in [`templates.py`](templates.py) from memory. Then start Blind 75.

## When to reach for what

Numbers match the banners in `templates.py`. Intervals, greedy, and 2-D DP are extra — no skeleton in that file.

| # | If you see… | Reach for | Typical complexity |
| --- | --- | --- | --- |
| 1 | Lookup, frequency, grouping, "have I seen this" | `dict` / `set` / `Counter` | O(1) avg lookup, O(n) space |
| 2 | Sorted pair, palindrome, opposite ends | Two pointers | O(n) after sort |
| 3 | Matching brackets, next greater, undo | Stack (`list`) | O(n) |
| 4 | BFS, level order, sliding-window queue | `collections.deque` | O(1) append/popleft |
| 5 | Sequential nodes, reverse, cycle, merge | Linked list + dummy / slow-fast | O(n) time, O(1) extra |
| 6 | Hierarchy, LCA, path, BST property | Tree DFS or BFS | O(n) |
| 7 | Shortest unweighted path, components, prerequisites | Graph BFS / DFS, Kahn topo | O(V + E) |
| 8 | Sorted array, min feasible value | Binary search on index or answer | O(log n) |
| 9 | Subarray / substring with a constraint | Sliding window | O(n) |
| 10 | kth / top-k / running median | `heapq` | O(log k) per push |
| 11 | "All combinations / permutations / paths" | Backtracking | Exponential; prune early |
| 12 | Min/max over subproblems | 1-D DP | O(n) or O(n * W) |
| 13 | Prefix dictionary / wildcard search | Trie | O(L) per word |
| — | Overlapping intervals | Sort by start, then merge | O(n log n) |
| — | Local choice that never needs undo | Greedy | Often O(n) after sort |
| — | Grid / two sequences | 2-D DP | O(m * n) |

## Python interview traps

- **Queue:** `deque.popleft()`. Never `list.pop(0)` (O(n)).
- **Heap:** `heapq` is a **min-heap**. Max-heap = push/pop negated values.
- **Slice copy:** `a[:]` and `a[l:r]` allocate a new list.
- **Mutable default:** `def f(xs=[])` shares one list. Use `None`.
- **Identity vs equality:** `==` for values, `is` for `None` (`x is None`).
- **Division:** `//` floor div, `/` float. Mid index: `(l + r) // 2`.
- **Recursion:** default limit ~1000. Prefer iterative BFS/DFS on huge graphs.
- **Sorting key:** `arr.sort(key=lambda x: x[0])` is in-place; `sorted` returns new.
- **Set/dict keys** must be hashable (no lists). Use `tuple`.
- **Grid visited:** mark in-place (`grid[r][c] = "#"`) or a `visited` set of tuples.

## Complexity you should say out loud

| Structure | Access | Search | Insert | Delete |
| --- | --- | --- | --- | --- |
| Array / list | O(1) | O(n) | O(n) middle / O(1) amort. end | O(n) |
| Hash map / set | — | O(1) avg | O(1) avg | O(1) avg |
| Stack / queue | O(1) ends | — | O(1) | O(1) |
| Heap | O(1) min | O(n) | O(log n) | O(log n) |
| BST (balanced) | — | O(log n) | O(log n) | O(log n) |
| Trie | — | O(L) | O(L) | O(L) |

## Resources

- [NeetCode roadmap](https://neetcode.io/roadmap) — topic order
- [Python collections](https://docs.python.org/3/library/collections.html)
- [heapq](https://docs.python.org/3/library/heapq.html)
- [Tech Interview Handbook cheatsheet](https://www.techinterviewhandbook.org/coding-interview-cheatsheet/)
