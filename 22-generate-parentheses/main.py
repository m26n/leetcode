from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                result.append("".join(stack))
                # stack.clear()
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return result


sol = Solution()
print(f"\n{sol.generateParenthesis(2)}\n")
