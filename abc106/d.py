# -*- coding: utf-8 -*-


def main():
    n, m, q = map(int, input().split())
    summed = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        li, ri = map(int, input().split())
        summed[li][ri] += 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            summed[i][j] += summed[i - 1][j]
            summed[i][j] += summed[i][j - 1]
            summed[i][j] -= summed[i - 1][j - 1]

    ans = list()

    for _ in range(q):
        pi, qi = map(int, input().split())
        count = summed[qi][qi] - summed[pi - 1][qi] - summed[qi][pi - 1] + summed[pi - 1][pi - 1]
        ans.append(count)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
