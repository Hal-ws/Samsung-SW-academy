T = int(input())
for test_case in range(1, T + 1):
    frogList = [[]]
    sound = input()
    if sound[0] != 'c':
        print('#%s %s' %(test_case, -1))
        continue
    frogList[0].append([1, 0, 0, 0, 0])
    for t in range(1, len(sound)):
        w = sound[t]
        endFlag = 0
        if w == 'c':
            newFlag = 1
            for i in range(len(frogList)):
                if frogList[i][-1][4] == 1: # 완성된 frog가 있을시
                    frogList[i].append([1, 0, 0, 0, 0])
                    newFlag = 0
                    break
            if newFlag: #새 개구리 추가해줘야됨
                frogList.append([])
                frogList[-1].append([1, 0, 0, 0, 0])
        else:
            if w == 'r':
                idx = 1
            if w == 'o':
                idx = 2
            if w == 'a':
                idx = 3
            if w == 'k':
                idx = 4
            flag = 1
            for i in range(len(frogList)):
                if frogList[i][-1][idx - 1] == 1 and frogList[i][-1][idx] == 0:
                    frogList[i][-1][idx] = 1
                    flag = 0
                    break
            if flag: # 넣을곳 없음
                endFlag = 1
        if endFlag:
            break
    if endFlag:
        ans = -1
    else:
        flag = 1
        for i in range(len(frogList)):
            if frogList[i][-1] != [1, 1, 1, 1, 1]:
                ans = -1
                flag = 0
                break
        if flag:
            ans = len(frogList)
    print('#%s %s' %(test_case, ans))
