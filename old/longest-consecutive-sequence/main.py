from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        uniq_nums = set(nums)
        seq = set()

        for n in nums:
          if n-1 in uniq_nums or n+1 in uniq_nums:
             seq.add(n)

        return len(seq)


solution = Solution()

input1 = [100,4,200,1,3,2]
expected_length = 4
seq1 = solution.longestConsecutive(input1)
assert len(seq1) == expected_length

input2 = [0,3,7,2,5,8,4,6,0,1]
expected_length = 9
seq2 = solution.longestConsecutive(input2)
assert len(seq2) == expected_length