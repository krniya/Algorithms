def evalRPN(tokens) -> int:
        notations = "+-/*"
        stack = []
        
        def sumOfNum(m,n):
            return m + n
        def diffOfNum(m,n):
            return m - n
        def mulOfNum(m,n):
            return m * n
        def divOfNum(m,n):
            return m // n
        
        for token in tokens:
            if token not in notations:
                stack.append(int(token))
                continue
            firstNum =  stack.pop()
            secondNum = stack.pop()
            if token == "+":
                stack.append(sumOfNum(firstNum, secondNum))
            elif token == "-":
                stack.append(diffOfNum(secondNum, firstNum))
            elif token == "*":
                stack.append(mulOfNum(firstNum, secondNum))
            elif token == "/":
                stack.append(divOfNum(secondNum, firstNum))
        return stack[-1]

def evalRPN(tokens) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
        
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))