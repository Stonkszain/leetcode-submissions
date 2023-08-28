class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        i = 0
        max_len = 0

        for j in range(len(s)):
            while s[j] in charSet:
                charSet.discard(s[i])
                i += 1
            charSet.add(s[j])
            max_len = max(max_len, j - i + 1)
        return max_len
