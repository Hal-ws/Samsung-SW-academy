from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = map(str, input().split())
    a, b = list(a), int(b)
    l = len(a)
    tmp = [a[i] for i in range(l)]
    absMax = sorted(tmp, reverse=True)
    tmp = ''
    for i in range(l):
        tmp += a[i]
    visit = set()
    ans = 0
    q = deque()
    q.append([a, 0])
    visit.add(tmp + '0')
    while len(q) > 0:
        numList, cnt = q[0][0], q[0][1]
        if numList == absMax:
            if (b - cnt) % 2 == 0:
                ans = ''
                for i in range(l):
                    ans += numList[i]
                break
        if cnt == b:
            tmp = ''
            for i in range(l):
                tmp += numList[i]
            tmp = int(tmp)
            if ans < tmp:
                ans = tmp
        for i in range(l - 1):
            for j in range(i + 1, l):
                if numList[i] <= numList[j]:
                    numList[i], numList[j] = numList[j], numList[i]
                    tmp = ''
                    for k in range(l):
                        tmp += numList[k]
                    if tmp + str(cnt + 1) not in visit and cnt + 1 <= b:
                        nxt = [numList[k] for k in range(l)]
                        visit.add(tmp + str(cnt + 1))
                        q.append([nxt, cnt + 1])
                    numList[i], numList[j] = numList[j], numList[i] # 원복함
                elif cnt == b - 1:
                    numList[i], numList[j] = numList[j], numList[i]
                    tmp = ''
                    for k in range(l):
                        tmp += numList[k]
                    if tmp + str(cnt + 1) not in visit and cnt + 1 <= b:
                        nxt = [numList[k] for k in range(l)]
                        visit.add(tmp + str(cnt + 1))
                        q.append([nxt, cnt + 1])
                    numList[i], numList[j] = numList[j], numList[i] # 원복함
        q.popleft()
    print('#%s %s' %(test_case, ans))
