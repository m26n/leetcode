from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            chars = [0] * 26
            for c in str:
                chars[ord(c) - ord("a")] += 1
            anagrams[tuple(chars)].append(str)
        return list(anagrams.values())


def main():
    strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]

    sol = Solution()
    print(sol.groupAnagrams(strs))


main()
