# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0.0

    for i in range(n):
        for j in range(i + 1, n):
            l, r = lr[i]
            nl, nr = lr[j]
            total = (r - l + 1) * (nr - nl + 1)
            met = 0

            for k in range(l, r + 1):
                met += max(0, min(k, nr + 1) - nl)

            ans += met / total

    print(ans)


if __name__ == "__main__":
    main()
