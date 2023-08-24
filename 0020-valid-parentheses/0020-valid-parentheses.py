class Solution:
    def isValid(self, s: str) -> bool:
        
        par_rev = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = list()

        for i in s:
            if i in ")}]":
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par_rev[i])

        return not stack
            
