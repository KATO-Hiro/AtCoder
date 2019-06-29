# -*- coding: utf-8 -*-


def main():
    n, k = map(int, input().split())
    max_comb = (n - 1) * (n - 2) // 2

    if k > max_comb:
        print(-1)
        exit()

    ans = list()
    candidates = list()

    for i in range(1, n):
        ans.append((1, i + 1))

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            candidates.append((i + 1, j + 1))

    for i in range(max_comb - k):
        ans.append(candidates[i])

    m = len(ans)
    print(m)

    for i in range(m):
        print(ans[i][0], ans[i][1])


if __name__ == '__main__':
    main()
