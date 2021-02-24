T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board = []
    t = int(input())
    for i in range(100):
        board.append(list(map(int, input().split())))
    ans = 0
    for i in range(100):
        tmp = sum(board[i])
        if ans < tmp:
            ans = tmp
    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += board[i][j]
        if ans < tmp:
            ans = tmp
    for i in range(100):
        tmp = 0
        tmp += board[i][i]
    if ans < tmp:
        ans = tmp
    for i in range(100):
        tmp = 0
        tmp += board[i][99 - i]
    if ans < tmp:
        ans = tmp
    print('#%s %s' %(test_case, ans))
