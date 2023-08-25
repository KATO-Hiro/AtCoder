# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, ai, bi, ci = map(int, input().split())

        if t != 1:
            break

        ans = 0

        for x in range(n + 1):
            for y in range(n + 1):
                if ((ai * x) + (bi * y)) % ci == 0:
                    ans += 1

        print(ans)


if __name__ == "__main__":
    main()
