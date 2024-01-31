#1
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for t in tokens:
            match t:
                case "+":
                    x = stack.pop()
                    y = stack.pop()
                    z = y + x
                    stack.append(z)
                case "-":
                    x = stack.pop()
                    y = stack.pop()
                    z = y - x
                    stack.append(z)
                case "*":
                    x = stack.pop()
                    y = stack.pop()
                    z = y * x
                    stack.append(z)
                case "/":
                    x = stack.pop()
                    y = stack.pop()
                    z = int(y / x)
                    stack.append(z)
                case _:
                    stack.append(int(t))


        return stack[0]

#2
class Solution:
    def resolves(self, a, b, Operator):
        if Operator == '+':
            return a + b
        elif Operator == '-':
            return a - b
        elif Operator == '*':
            return a * b
        return int(a / b)

    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                integer2 = stack.pop()
                integer1 = stack.pop()
                operator = token
                resolved_ans = self.resolves(integer1, integer2, operator)
                stack.append(resolved_ans)
            else:
                stack.append(int(token))
        return stack.pop()
