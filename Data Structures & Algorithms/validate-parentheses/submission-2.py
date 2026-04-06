from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                a = stack.pop()
                if a == '(' and i == ')':
                    continue
                if a == '[' and i == ']':
                    continue
                if a == '{' and i == '}':
                    continue
                return False
        if len(stack) > 0:
            return False
        return True