class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        char_offset = ord("a")
        alphabet = [0] * 26
        for i in range(len(s)):
            alphabet[ord(s[i]) - char_offset] += 1
            alphabet[ord(t[i]) - char_offset] -= 1
        return all(value == 0 for value in alphabet)
