T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_tmpase in range(1, T + 1):
    l = int(input())
    stack = []
    infix = input()
    postfix = []
    for i in range(l):
        tmp = infix[i]
        if tmp == '(':
            stack.append(tmp)
        elif tmp == ')':
            while 1:
                top = stack.pop()
                if top == '(':
                    break
                else:
                    postfix.append(top)
        elif tmp == '+':
            while len(stack) > 0:
                top = stack.pop()
                if top == '(' or top == ')':
                    stack.append(top)
                    break
                else:
                    postfix.append(top)
            stack.append(tmp)
        elif tmp == '*':
            while len(stack) > 0:
                top = stack.pop()
                if top == '*':
                    postfix.append(top)
                else:
                    stack.append(top)
                    break
            stack.append(tmp)
        else:
            postfix.append(int(tmp))
    while len(stack) > 0:
        postfix.append(stack.pop())
    stack = []
    for i in range(len(postfix)):
        if postfix[i] == '+':
            v1, v2 = stack.pop(), stack.pop()
            stack.append(v1 + v2)
        elif postfix[i] == '*':
            v1, v2 = stack.pop(), stack.pop()
            stack.append(v1 * v2)
        else:
            stack.append(postfix[i])
    print('#%s %s' %(test_tmpase, stack[0]))
