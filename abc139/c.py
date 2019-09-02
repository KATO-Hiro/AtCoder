# -*- coding: utf-8 -*-


def main():
    n = int(input())
    h = list(map(int, input().split()))[::-1]
    ans = [0 for _ in range(n)]

    for i in range(1, n):
        if h[i] >= h[i - 1]:
            ans[i] += ans[i - 1] + 1

    print(max(ans))


if __name__ == '__main__':
    main()
