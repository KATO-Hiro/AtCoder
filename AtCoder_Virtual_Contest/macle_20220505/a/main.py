# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    p, q = divmod(n, a + b)
    ans = p * a + min(q, a)
    print(ans)


if __name__ == "__main__":
    main()
