import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ({"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv})

        for char in tokens:
            if char not in operations:
                stack.append(int(char))
            else:
                first = stack.pop()
                second = stack.pop()
                res = int(operations[char](second, first))

                stack.append(res)

        return stack[-1]
