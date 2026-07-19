# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for _ in range(n):
        ai, bi, si = input().rstrip().split()
        ai = int(ai)
        bi = int(bi)

        if si == "keep":
            ans += bi - ai

    print(ans)


if __name__ == "__main__":
    main()
