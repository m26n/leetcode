class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not (s[left]).isalnum():
                left += 1
                continue
            if not (s[right]).isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


solution = Solution()

input1 = "A man, a plan, a canal: Panama"
output1 = True
assert solution.isPalindrome(input1) == output1

input2 = "race a car"
output2 = False
assert solution.isPalindrome(input2) == output2

input3 = " "
output3 = True
assert solution.isPalindrome(input3) == output3
