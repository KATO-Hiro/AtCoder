# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, t, x, y = map(int, input().split())
    p = [int(input()) for _ in range(m)]
    scores = [p.copy() for _ in range(n)]
    ans = [0] * n

    for _ in range(y):
        tk, nk, mk, result = input().rstrip().split()
        tk, nk, mk = int(tk), int(nk), int(mk)
        nk -= 1
        mk -= 1

        if result == "open":
            scores[nk][mk] += tk
        elif result == "incorrect":
            scores[nk][mk] -= 120
        else:
            scores[nk][mk] -= tk
            ans[nk] += max(scores[nk][mk], x)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
