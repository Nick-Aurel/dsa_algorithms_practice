"""
LC 424 — Longest Repeating Character Replacement | Medium | Sliding Window
Pattern: window valid while (len - max_freq) <= k
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    print("ok")
