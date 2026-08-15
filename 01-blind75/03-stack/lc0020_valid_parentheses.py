"""
LC 20 — Valid Parentheses | Easy | Stack
Pattern: matching brackets (push openers, pop on closer)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""


class Solution:
    def isValid(self, s: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    print("ok")
