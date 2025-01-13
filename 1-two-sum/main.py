from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            if n in indices:
                return [i, indices[n]]
            indices[target - n] = i

