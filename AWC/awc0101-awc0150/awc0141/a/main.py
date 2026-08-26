# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, s, e = map(int, input().split())
    ans = 0

    for _ in range(n):
        ti, hi, bi = map(int, input().split())

        if (s <= ti <= e) and (hi >= k):
            ans += bi

    print(ans)


if __name__ == "__main__":
    main()
