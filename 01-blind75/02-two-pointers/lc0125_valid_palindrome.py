"""
LC 125 — Valid Palindrome | Easy | Two Pointers
Pattern: opposite ends; skip non-alphanumeric
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    print("ok")
