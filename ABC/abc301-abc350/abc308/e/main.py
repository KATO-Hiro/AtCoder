# -*- coding: utf-8 -*-


def mex(x, y, z):
    used = [False] * 4

    for i in [x, y, z]:
        used[i] = True

    for i, u in enumerate(used):
        if not u:
            return i


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    s = input().rstrip()

    # jを固定 + i < j、j < kとなる個数を累積和で計算
    acc_m = [[0 for _ in range(n)] for _ in range(3)]
    acc_x = [[0 for _ in range(n)] for _ in range(3)]

    for i, (si, ai) in enumerate(zip(s, a)):
        if i > 0:
            for y in range(3):
                acc_m[y][i] = acc_m[y][i - 1]
                acc_x[y][i] = acc_x[y][i - 1]

        if si == "M":
            acc_m[ai][i] += 1
        elif si == "X":
            acc_x[ai][i] += 1

    ans = 0

    for j, (si, ai) in enumerate(zip(s, a)):
        if j == 0 or j == n - 1:
            continue

        if si != "E":
            continue

        for x in range(3):
            for y in range(3):
                ans += acc_m[x][j - 1] * (acc_x[y][n - 1] - acc_x[y][j]) * mex(x, y, ai)

    print(ans)


if __name__ == "__main__":
    main()
