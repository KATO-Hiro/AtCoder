# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    ans = 0

    if a <= b:
        ans = max(0, n - (a - 1))
    else:
        p, q = divmod(n, a)

        if p >= 1:
            ans = (p - 1) * b
            ans += min(b, q + 1)

    print(ans)


if __name__ == "__main__":
    main()
