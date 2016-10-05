#!/usr/bin/env python3

def calculate(myarg):
    stack = []
    for token in myarg.split():
        if token == '+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg1 + arg2
            stack.append(result)
        elif token == '*':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg1 * arg2
            stack.append(result)
        elif token == '/':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 / arg2
            stack.append(result)
        elif token == '-':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 - arg2
            stack.append(result)
        else:
            stack.append(int(token))
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too Many params")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc>"))
        print(result)

if __name__ == '__main__':
    main()
