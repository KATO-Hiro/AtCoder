# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [input().rstrip() for _ in range(n)]
    win = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if s[i][j] == "o":
                win[i] += 1

    tmp = list()

    for i, wi in enumerate(win):
        tmp.append((wi, i))

    tmp.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    ans = list()

    for i, (_, ti) in enumerate(tmp):
        ans.append(ti + 1)

    print(*ans)


if __name__ == "__main__":
    main()
