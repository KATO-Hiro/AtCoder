# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, t = map(int, input().split())

    for _ in range(n):
        xi, vi = map(int, input().split())
        total = xi + vi * t

        p, q = divmod(total, l)

        if p % 2 == 0:
            ans = q
        else:
            ans = l - q

        print(ans)


if __name__ == "__main__":
    main()
