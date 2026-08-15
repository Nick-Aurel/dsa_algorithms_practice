"""
LC 139 — Word Break | Medium | 1-D DP
Pattern: dp[i] = prefix s[:i] can be segmented
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("ok")
