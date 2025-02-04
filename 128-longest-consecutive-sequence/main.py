from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence_length = 0

        for n in nums_set:
            if (n - 1) not in nums_set:
                length = 1
                while (n + length) in nums_set:
                    length += 1
                max_sequence_length = max(length, max_sequence_length)
        return max_sequence_length


nums = [2, 20, 4, 10, 3, 4, 5]
expected = 4
sol = Solution()
actual = sol.longestConsecutive(nums)
assert expected == actual
