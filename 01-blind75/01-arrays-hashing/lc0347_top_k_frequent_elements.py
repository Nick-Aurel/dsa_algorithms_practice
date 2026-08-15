"""
LC 347 — Top K Frequent Elements | Medium | Arrays & Hashing
Pattern: Counter + heap (or bucket sort)
Time:      Space:
Attempt:   min | Hint: yes/no | Recoded: yes/no
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        raise NotImplementedError


if __name__ == "__main__":
    s = Solution()
    assert set(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert s.topKFrequent([1], 1) == [1]
    print("ok")
