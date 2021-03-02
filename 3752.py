from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    nList = list(map(int, input().split()))
    scoreChk = [0] * 10001
    q = deque()
    q.append([0, 1]) #틀림
    q.append([nList[0], 1]) #맞음
    scoreChk[0] = 1
    scoreChk[nList[0]] = 1
    while len(q) > 0:
        tmp = q.popleft()
        score, idx = tmp[0], tmp[1]
        if idx == N:
            continue
        rightScore = score + nList[idx]
        if scoreChk[rightScore] == 0:
            scoreChk[rightScore] = 1
            q.append([rightScore, idx + 1])
        q.append([score, idx + 1])
    print('#%s %s' %(test_case, sum(scoreChk)))
