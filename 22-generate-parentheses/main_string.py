from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_n, closed_n, path):
            if open_n == closed_n == n:
                result.append(path)
                return
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")

        backtrack(0, 0, "")
        return result


sol = Solution()
print(f"\n{sol.generateParenthesis(3)}\n")
