class Solution:

    def isPalindrome(self, s: str) -> bool:

        def valid_char(c):
            if (ord(c.lower()) in range(ord("a"), ord("z") + 1) 
            or ord(c.lower()) in range(ord("0"), ord("9") + 1)):
                return True
            return False

        l, r = 0, len(s) - 1

        while l < r:
            if not valid_char(s[l]):
                l += 1
                continue
            if not valid_char(s[r]):
                r -= 1
                continue
            if not s[l].lower() == s[r].lower():
                return False
            l += 1
            r -= 1

        return True

