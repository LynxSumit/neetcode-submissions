class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in ['+', '-', '*', '/']:
                stack.append(int(item))
            else:
                el2 = int(stack.pop())
                el1 = int(stack.pop())
                if item == '+':
                    stack.append(el1 + el2)
                elif item == '-':
                    print(el1, el2)
                    stack.append(el1 - el2)
                elif item == '*':
                    stack.append(el1 * el2)
                else:
                    stack.append(int(el1 / el2))
        return stack[0]