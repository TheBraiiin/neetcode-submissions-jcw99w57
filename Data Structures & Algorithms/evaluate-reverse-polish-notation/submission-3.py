class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(int(stack.pop() + stack.pop()))
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif token == '*':
                stack.append(int(stack.pop() * stack.pop()))
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack.pop()




#["10","6","9","3","+","-11","*","/","*","17","+","5","+"] => 

#10 * (6 / ((9+3) * -11)) + 17 + 5
 
#   
#   2  
#  10

#    (3 + 9)