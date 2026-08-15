"""
LC 49 — Group Anagrams | Medium | Arrays & Hashing
Pattern: hash map grouping (sorted key or count tuple)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        raise NotImplementedError


def _normalized(groups: List[List[str]]) -> List[List[str]]:
    return sorted((sorted(g) for g in groups), key=lambda g: (len(g), g))


if __name__ == "__main__":
    s = Solution()
    got = _normalized(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    expected = _normalized([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert got == expected
    assert _normalized(s.groupAnagrams([""])) == [[""]]
    assert _normalized(s.groupAnagrams(["a"])) == [["a"]]
    print("ok")
