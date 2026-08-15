"""
LC 242 — Valid Anagram | Easy | Arrays & Hashing
Pattern: frequency / Counter
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    print("ok")
