def main():
    T = int(input())
    for t in range(T):
        D, L, N = map(int, input().split())
        first = D
        last = D + (L * D // 100) * (N - 1)
        ans = N * (first + last) // 2
        print('#%s %s' %(t + 1, ans))


if __name__ == '__main__':
    main()
