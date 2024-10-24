# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    p, q = map(int, input().split())
    a, b = map(int, input().split())

    ans = min(p, q) * a + max(0, q - p) * b
    print(ans)


if __name__ == "__main__":
    main()
