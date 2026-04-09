class Solution:
    def isValid(self, st: str) -> bool:
        i = 0
        s = []
        while i < len(st):
            if s and s[-1] == '(' and st[i] == ')':
                s.pop()
            elif s and s[-1] == '{' and st[i] == '}':
                s.pop()
            elif s and s[-1] == '[' and st[i] == ']':
                s.pop()
            else:
                s.append(st[i])
            i+=1
        return len(s) == 0