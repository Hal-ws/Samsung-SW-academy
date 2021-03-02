from collections import deque


T = 10
dy, dx = [0, 0, -1], [-1, 1, 0]
for test_case in range(1, T + 1):
    t = int(input())
    q = deque()
    board = []
    visit = [[0 for j in range(100)] for i in range(100)]
    for i in range(100):
        board.append(list(map(int, input().split())))
    for j in range(100):
        if board[99][j] == 2:
            visit[i][j] = 1
            q.append([i, j])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        flag = 0
        if y == 0:
            ans = x
            break
        for i in range(3):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 100 and 0 <= nx < 100 and visit[ny][nx] == 0 and board[ny][nx] == 1:
                if i == 0 or i == 1:
                    flag = 1
                visit[ny][nx] = 1
                q.append([ny, nx])
            if flag:
                break
    print('#%s %s' %(t, ans))
