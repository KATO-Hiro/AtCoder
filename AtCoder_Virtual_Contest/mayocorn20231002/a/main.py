# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p, q = divmod(n, 5)
    ans = p * 5

    if q >= 3:
        ans += 5

    print(ans)


if __name__ == "__main__":
    main()
