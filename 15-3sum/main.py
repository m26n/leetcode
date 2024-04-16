from collections import defaultdict
from typing import List

# copied from neetcode
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


sol = Solution()

input1 = [-1, 0, 1, 2, -1, -4]
output1 = [[-1, -1, 2], [-1, 0, 1]]
three_sum = sol.threeSum(input1)
assert output1 == three_sum

input2 = [0, 1, 1]
output2 = []
three_sum = sol.threeSum(input2)
assert output2 == three_sum

input3 = [0, 0, 0]
output3 = [[0, 0, 0]]
three_sum = sol.threeSum(input3)
assert output3 == three_sum
