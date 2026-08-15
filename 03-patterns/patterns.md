# Pattern map

Internalize the **move**, not the solution. After each problem, add it to the row you used.

## Hash map

**Move:** complement, frequency, grouping, seen-index.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Two Sum | Blind 75 | value → index, look up `target - x` |
| Contains Duplicate | Blind 75 | set membership |
| Valid Anagram | Blind 75 | frequency / Counter |
| Group Anagrams | Blind 75 | sorted-key or count-tuple grouping |
| Longest Consecutive Sequence | Blind 75 | set; only start a streak from `x-1` missing |

## Two pointers

**Move:** sorted pairs, opposite ends, fast/slow.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Valid Palindrome | Blind 75 | skip non-alnum, compare inward |
| 3Sum | Blind 75 | sort + fixed i + two-sum; skip dupes |
| Container With Most Water | Blind 75 | move the shorter height |

## Sliding window

**Move:** grow `r`; shrink `l` while invalid; track counts.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Best Time to Buy/Sell Stock | Blind 75 | running min (window of one buy) |
| Longest Substring Without Repeating | Blind 75 | last-seen index or set |
| Longest Repeating Character Replacement | Blind 75 | window valid if `len - maxfreq <= k` |
| Minimum Window Substring | Blind 75 stretch | need vs have counts |

## Stack

**Move:** matching, next greater, monotonic.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Valid Parentheses | Blind 75 | push openers, pop on match |

## Binary search

**Move:** search space **is** the answer; prove the predicate; watch mid bias.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Find Min in Rotated Sorted Array | Blind 75 | compare mid vs right |
| Search in Rotated Sorted Array | Blind 75 | which half is sorted, then in-range? |

## Linked list

**Move:** dummy, reverse in place, fast/slow, merge.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Reverse Linked List | Blind 75 | prev/curr/nxt |
| Merge Two Sorted Lists | Blind 75 | dummy + tail |
| Linked List Cycle | Blind 75 | Floyd slow/fast |
| Remove Nth From End | Blind 75 | dummy + two pointers n apart |
| Reorder List | Blind 75 | mid + reverse second + merge |
| Merge K Sorted Lists | Blind 75 stretch | heap of heads |

## Tree DFS / BFS

**Move:** return value up; mutate; path + backtrack. BFS = queue + level-size loop.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Invert / Max Depth / Same / Subtree | Blind 75 | recursive structure |
| Level Order | Blind 75 | BFS `for _ in range(len(q))` |
| Validate BST | Blind 75 | carry lo/hi bounds |
| LCA of BST | Blind 75 | walk by value |
| Kth Smallest in BST | Blind 75 | inorder count |
| Construct Pre+In | Blind 75 stretch | inorder index map |
| Max Path Sum / Serialize | Blind 75 stretch | postorder return |

## Heap

**Move:** kth / top-k / running median. Min-heap of size k, or two heaps.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Top K Frequent | Blind 75 | Counter + min-heap of size k |
| Find Median from Data Stream | Blind 75 | lo max-heap / hi min-heap |

## Intervals

**Move:** sort by start; merge if `curr.start <= prev.end`.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Merge Intervals | Blind 75 | sort + sweep |
| Insert Interval | Blind 75 | left / overlap / right |
| Non-overlapping Intervals | Blind 75 | greedy by end |

## Backtracking

**Move:** choose / explore / unchoose; prune; in-place mark on grids.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Combination Sum | Blind 75 | reuse index `i` vs `i+1` |
| Word Search | Blind 75 | DFS + mark cell |

## Graph

**Move:** visited; BFS for layers; 3-color / recursion stack for directed cycle; Kahn for topo.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Number of Islands | Blind 75 | DFS/BFS flood fill |
| Clone Graph | Blind 75 | map old → new |
| Course Schedule | Blind 75 | cycle or Kahn |
| Pacific Atlantic | Blind 75 | multi-source DFS from oceans |

## 1-D DP / greedy

**Move:** name `dp[i]`, recurrence, base, iterate order. Greedy = local choice + invariant.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Climbing Stairs | Blind 75 | Fibonacci |
| House Robber / II | Blind 75 | skip vs take; circular = two ranges |
| Coin Change | Blind 75 | unbounded knapsack min |
| Word Break | Blind 75 | `dp[i]` = prefix breakable |
| Maximum Subarray | Blind 75 | Kadane |
| Jump Game | Blind 75 | farthest reachable |

## 2-D DP (lite)

**Move:** `dp[r][c]` from top/left or two strings.

| Problem | List | Pattern detail |
| --- | --- | --- |
| Unique Paths | Blind 75 stretch | `dp[r][c] = up + left` |

## Tries / bits / advanced graphs / math

Skip in the 3-day core. After the interview, add rows here as you solve NeetCode 150 extras.
