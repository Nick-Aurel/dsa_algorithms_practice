"""
LC 3 — Longest Substring Without Repeating Characters | Medium | Sliding Window
Pattern: grow r, shrink l; last-seen index or set
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    print("ok")
