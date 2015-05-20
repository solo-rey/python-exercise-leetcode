class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens or len(tokens) == 0:
            return 0
        stack = []
        for i in range(len(tokens)):
            if len(tokens[i])>1 or tokens[i].isdigit():
                stack.append(tokens[i])
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if tokens[i] == '+':
                    tmp = int(num1)+int(num2)
                    stack.append(str(tmp))
                if tokens[i] == '-':
                    tmp=int(num2)-int(num1)
                    stack.append(str(tmp))
                if tokens[i] == '*':
                    tmp=int(num2)*int(num1)
                    stack.append(str(tmp))
                if tokens[i] == '/':
                    tmp=float(num2)/float(num1)
                    stack.append(str(int(tmp)))
        return int(stack.pop())

s = Solution()
print s.evalRPN( ["10","6","9","3","+","-11","*","/","*","17","+","5","+"])