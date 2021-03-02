from collections import deque


T = int(input())
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
for test_case in range(1, T + 1):
    board = []
    q = deque()
    ansSet = set()
    for i in range(4):
        board.append(list(map(int, input().split())))
    for i in range(4):
        for j in range(4):
            q.append([str(board[i][j]), i, j, 1])
            while len(q) > 0:
                tmp = q.popleft()
                num, y, x, l = tmp[0], tmp[1], tmp[2], tmp[3]
                if l == 7:
                    ansSet.add(num)
                    continue
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < 4 and 0 <= nx < 4:
                        q.append([num + str(board[ny][nx]), ny, nx, l + 1])
    ans = len(list(ansSet))
    print('#%s %s' %(test_case, ans))
