class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            elif len(stack) == 0:
                return False
            elif x == ')':
                ch = stack.pop()
                if ch != '(':
                    return False
            elif x == '}':
                ch = stack.pop()
                if ch != '{':
                    return False
            elif x == ']':
                ch = stack.pop()
                if ch != '[':
                    return False
        
        if len(stack) != 0:
            return False
        
        return True