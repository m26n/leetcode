class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric = ""
        for c in s:
            if c.isalnum():
                alpha_numeric += c.lower()
        return alpha_numeric == alpha_numeric[::-1]

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
