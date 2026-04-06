class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                b += a
                stack.append(b)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                b -= a
                stack.append(b)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                b *= a
                stack.append(b)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                b = int(b / a)
                stack.append(b)
            else:
                stack.append(int(i))
        return stack.pop()