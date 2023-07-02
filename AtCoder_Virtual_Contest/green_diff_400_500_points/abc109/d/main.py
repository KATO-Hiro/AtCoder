# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = list()

    for i in range(h):
        for j in range(w - 1):
            if a[i][j] > 0 and a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))

    for i in range(h - 1):
        j = w - 1

        if a[i][j] > 0 and a[i][j] % 2 == 1:
            a[i][j] -= 1
            a[i + 1][j] += 1
            ans.append((i + 1, j + 1, i + 2, j + 1))

    print(len(ans))

    for yi, xi, yj, xj in ans:
        print(yi, xi, yj, xj)


if __name__ == "__main__":
    main()
