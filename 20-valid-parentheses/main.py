from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = deque()
        open_brackets = set("([{")
        bracket_pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif stack and stack[-1] == bracket_pairs[c]:
                stack.pop()
            else:
                return False
        return True if not stack else False


sol = Solution()
s = ")["
print(sol.isValid(s))
