# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, m, l = map(int, input().split())
    ans = 10**18

    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if (i * 6 + j * 8 + k * 12) >= n:
                    ans = min(ans, i * s + j * m + k * l)

    print(ans)


if __name__ == "__main__":
    main()
