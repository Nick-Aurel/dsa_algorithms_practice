# DSA interview practice (Python)

3-day FAANG-style prep. **Pattern fluency**, not a completion badge.

Blind 75 + NeetCode 150 in 3 days is not realistic if you want to remember it in the room. Follow the schedule below. NeetCode 150 extras wait until after the interview.

| Must do | If time | After the interview |
| --- | --- | --- |
| DS refresher + ~40 Blind 75 **core** problems, roadmap order | Remaining Blind 75 (hard trees, 2-D DP, bit, tries) | NeetCode 150 extras in `02-neetcode150/` |

Target: **8–10 focused hours/day**. Timed practice beats watching videos.

## How to study (non-negotiable)

For every problem:

1. **2 min** — restate, constraints, brute force, target complexity
2. **Timer on** — Easy 15 min, Medium 25 min, Hard 40 min
3. **Stuck at 50% time** — one hint (pattern name only), keep coding
4. **Still stuck** — read the NeetCode solution / video at 1.5x, **close it**, recode from blank in 10 min
5. **Speak out loud** as if the interviewer is there
6. **Never copy-paste** a solution into this repo

Skip a Hard if it is blocking the next 3 Mediums. Mark it in [TRACKING.md](TRACKING.md) and move.

Check the box in `TRACKING.md` only after you can recode it from memory.

## Hour 0 — data structure refresher (2–3 hours)

Implement the snippets in [`00-refresher/templates.py`](00-refresher/templates.py) **from memory**. If you cannot write it, you cannot use it under pressure.

Then skim [`00-refresher/cheatsheet.md`](00-refresher/cheatsheet.md). Do **not** watch a 10-hour DS course.

## 3-day schedule (NeetCode roadmap order)

```
Hour 0 templates
  → Day 1 Arrays/Hashing, Two Pointers, Stack, Sliding Window, Binary Search
  → Day 2 Linked List, Trees, Heap, Intervals
  → Day 3 Graphs, Backtracking, 1-D DP, Greedy, mocks
  → After: NC150 extras, Tries, 2-D DP, Advanced Graphs
```

Exact problem checkboxes: [TRACKING.md](TRACKING.md).

### Day 1 — linear structures

**Morning (after templates):** Arrays & Hashing, Two Pointers, Stack  
**Afternoon:** Sliding Window, Binary Search  
**Night (45 min):** 1 Easy + 1 Medium, timed, no notes. Log in [`04-mocks/day1.md`](04-mocks/day1.md).

Day 1 core stubs (open and type):

- `01-blind75/01-arrays-hashing/`
- `01-blind75/02-two-pointers/`
- `01-blind75/03-stack/`
- `01-blind75/04-binary-search/`
- `01-blind75/05-sliding-window/`

### Day 2 — linked lists + trees

**Morning:** Linked List  
**Afternoon:** Trees (core), Heap if time, Intervals  
**Night mock:** tree BFS/DFS medium + one linked list → [`04-mocks/day2.md`](04-mocks/day2.md)

Create Day 2 files the same way as Day 1: `lc0XXX_name.py` with the docstring header.

### Day 3 — graphs, DP, interview simulation

**Morning:** Graphs + Backtracking (skip Tries unless core is done)  
**Afternoon:** 1-D DP + Greedy; **one** 2-D DP (Unique Paths) then stop  
**Late afternoon (2 hours):** two 45-min mocks. Speak the whole time. Recode your 5 weakest from blank.  
**Evening:** skim templates + [`03-patterns/patterns.md`](03-patterns/patterns.md) only. Sleep.

Skip for 3 days: Bit Manipulation, Math & Geometry, Advanced Graphs, Word Search II, most 2-D DP.

## Folder layout

```
00-refresher/          templates + cheatsheet
01-blind75/            Blind 75, numbered 01–18 by roadmap topic
02-neetcode150/        extras only (same 01–18 folders)
03-patterns/           pattern → problem map
04-mocks/              timed mock logs + rubric
PROMPT.md              paste this into a coaching chat
TRACKING.md            core / stretch / later checkboxes
```

One Python file per problem: `lc0001_two_sum.py`.

```python
"""
LC 1 — Two Sum | Easy | Arrays & Hashing
Pattern: hash map complement
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
```

## Resources (use in this order)

1. Problem lists: [Blind 75 / NeetCode 150](https://neetcode.io/practice)
2. If stuck: NeetCode YouTube for **that one** problem at 1.5x — not a playlist binge
3. Python: `typing`, `deque`, `heapq`, `Counter`
4. Interview behavior: [coding rubric](https://www.techinterviewhandbook.org/coding-interview-rubric/)
5. After the interview: [Grind 75](https://www.techinterviewhandbook.org/grind75) if you get another loop with more days

Do not add more lists. One roadmap, one language, one repo.

## Coaching

Copy [PROMPT.md](PROMPT.md) at the start of a session. You write the code; the coach does not dump solutions first.
