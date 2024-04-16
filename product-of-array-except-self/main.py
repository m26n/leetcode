from typing import List
# result
# [1  , 3,12,72]
# suffix = 1 * 7 * 6 * 4 * 3
# [168,126,84,72]

# [3  , 4, 6, 7]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(solution.productExceptSelf([3  , 4, 6, 7]))  # [24, 12, 8, 6]
