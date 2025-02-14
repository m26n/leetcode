import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set("+-*/")
        for t in tokens:
            if t in operators:
                n2 = stack.pop()
                n1 = stack.pop()
                match t:
                    case "+":
                        stack.append(n1 + n2)
                    case "-":
                        stack.append(n1 - n2)
                    case "*":
                        stack.append(n1 * n2)
                    case "/":
                        stack.append(math.trunc(n1 / n2))
            else:
                stack.append(int(t))
        return stack.pop()


solution = Solution()
input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(solution.evalRPN(input))
