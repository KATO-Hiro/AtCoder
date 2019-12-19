# -*- coding: utf-8 -*-


def left_90(n, s, t):
    cost = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[n - j + 1][i] != t[i][j]:
                cost += 1

    return cost


def right_90(n, s, t):
    cost = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[j][n - i + 1] != t[i][j]:
                cost += 1

    return cost


def left_180(n, s, t):
    cost = 2

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[n + 1 - i][n + 1 - j] != t[i][j]:
                cost += 1

    return cost


def default(n, s, t):
    cost = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i][j] != t[i][j]:
                cost += 1

    return cost


def main():
    n = int(input())

    s = list()
    s.append('I' * (n + 2))
    t = list()
    t.append('I' * (n + 2))

    for i in range(n):
        s.append('I' + input() + 'I')

    s.append('I' * (n + 2))

    for i in range(n):
        t.append('I' + input() + 'I')

    t.append('I' * (n + 2))

    ans = float('inf')

    # 反時計回りに90度回転
    ans = min(ans, left_90(n, s, t))
    # 時計回りに90度回転
    ans = min(ans, right_90(n, s, t))
    # 180度回転
    ans = min(ans, left_180(n, s, t))
    # マスを一つずつ塗り替え
    ans = min(ans, default(n, s, t))
    print(ans)


if __name__ == '__main__':
    main()
