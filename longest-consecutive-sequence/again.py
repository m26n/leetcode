from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        longest = 0

        for n in uniq_nums:
            if n-1 not in uniq_nums:
                length = 1
                while n+length in uniq_nums:
                    length += 1
                longest = max(longest, length)

        return longest


solution = Solution()

input1 = [100,4,200,1,3,2]
expected_length = 4
seq1 = solution.longestConsecutive(input1)
assert seq1 == expected_length

input2 = [0,3,7,2,5,8,4,6,0,1]
expected_length = 9
seq2 = solution.longestConsecutive(input2)
assert seq2 == expected_length

input3 = [0,0]
expected_length = 1
seq3 = solution.longestConsecutive(input3)
assert seq3 == expected_length