class Solution:
    def countSubstrings(self, s: str) -> int:

        # Idea 1: two pointers
        # 
        #

        result = 0 # result counter

        # for loop iterating through the indicies of s
        for i in range(len(s)):
            # checking odd numbered palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: # checks if pointers are valid and if valid palindrome
                result += 1 # increments result
                l -= 1
                r += 1
            # checking even numbered palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: # checks if pointers are valid and if valid palindrome
                result += 1
                l -= 1
                r += 1

        return result

