# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = float("inf")

    for b in range(62):
        a, c = divmod(n, 2 ** b)
        ans = min(ans, a + b + c)

    print(ans)


if __name__ == "__main__":
    main()
