class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el.isdigit() or (el[0] == '-' and el[1:].isdigit()):  # Handles negative numbers
                stack.append(int(el))
            else:
                i = stack.pop()
                j = stack.pop()
                if el == '+':
                    stack.append(j + i)
                elif el == '*':
                    stack.append(j * i)
                elif el == '/':
                    stack.append(int(j / i))  # Integer division that truncates toward 0
                elif el == '-':
                    stack.append(j - i)

        return stack.pop()


                