# -*- coding: utf-8 -*-


def main():
    n, m, q = map(int, input().split())
    lr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    c = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        li, ri = map(int, input().split())
        lr[li][ri] += 1

    for i in range(n + 1):
        for j in range(n + 1):
            c[i][j] = c[i][j - 1] + lr[i][j]

    ans = list()

    for _ in range(q):
        pi, qi = map(int, input().split())
        count = 0

        for i in range(pi, qi + 1):
            count += c[i][qi] - c[i][pi - 1]

        ans.append(count)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
