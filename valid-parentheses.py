def isValid(self, s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0 or s[i] == '(' or s[i] == '[' or s[i] == '{':
            stack.append(s[i])
        else:
            if s[i] == ')' and stack[-1] != '(':
                return False
            if s[i] == ']' and stack[-1] != '[':
                return False
            if s[i] == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return len(stack) == 0