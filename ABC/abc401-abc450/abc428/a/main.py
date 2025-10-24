# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, a, b, x = map(int, input().split())
    c = a + b
    p, q = divmod(x, c)
    ans = p * a * s
    ans += min(q, a) * s

    print(ans)


if __name__ == "__main__":
    main()
