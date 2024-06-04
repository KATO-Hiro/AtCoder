# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    ans = (
        [i for i in range(1, l)]
        + [i for i in range(l, r + 1)][::-1]
        + [i for i in range(r + 1, n + 1)]
    )
    print(*ans)


if __name__ == "__main__":
    main()
