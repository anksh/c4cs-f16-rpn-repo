#!/usr/bin/env python3

import operator

operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow,
            }


def calculate(myarg):
    stack = []
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
           function = operators[token]
           arg2 = stack.pop()
           arg1 = stack.pop()
           stack.append(function(arg1, arg2))
    if len(stack) != 1:
        raise TypeError("Too Many params")
    return stack.pop()

def main():
    a = {'a':'b',
'a':'b',
'a':'b',
'a':'b',
'a':'b',
    }
    while True:
        result = calculate(input("rpn calc>"))
        print(result)

if __name__ == '__main__':
    import antigravity
    main()
