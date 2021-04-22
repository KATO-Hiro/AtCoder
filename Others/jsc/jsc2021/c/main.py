# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    ans = 1

    for i in range(1, b):
        z = ceil(a / i)

        if i * (z + 1) <= b:
            ans = max(ans, i)

    print(ans)


if __name__ == "__main__":
    main()
