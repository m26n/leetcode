from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        super_string = ""
        for i,s in enumerate(strs):
            super_string += s
            if i < len(strs) - 1:
              super_string += "'''"
        return super_string


    def decode(self, s: str) -> List[str]:
        return s.split("'''")

sol = Solution()
input = ["neet","code","love","you"]
encoded = sol.encode(input)
print(encoded)
decoded = sol.decode(encoded)
print(decoded)
assert input == decoded

input2 = ["we","say",":","yes"]
encoded2 = sol.encode(input2)
print(encoded2)
decoded2 = sol.decode(encoded2)
print(decoded2)
assert input2 == decoded2

