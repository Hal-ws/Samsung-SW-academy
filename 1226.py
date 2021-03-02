from collections import deque


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
for test_case in range(1, T + 1):
    ans = 0
    board = []
    case = int(input())
    for i in range(16):
        board.append(input())
    q = deque()
    eFlag = 0
    visit = [[0 for j in range(16)] for i in range(16)]
    for i in range(16):
        for j in range(16):
            if board[i][j] == '2':
                q.append([i, j])
                visit[i][j] = 1
                while len(q) > 0:
                    y, x = q.popleft()
                    if board[y][x] == '3':
                        ans = 1
                        eFlag = 1
                        break
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < 16 and 0 <= nx < 16 and visit[ny][nx] == 0 and board[ny][nx] != '1':
                            q.append([ny, nx])
                            visit[ny][nx] = 1
                break
        if eFlag:
            break
    print('#%s %s' %(test_case, ans))
