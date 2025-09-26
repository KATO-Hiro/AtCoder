# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, c = map(int, input().split())
    ans = 0

    for candidate in range(0, x + 1, 1000):
        if candidate * (1000 + c) > 1000 * x:
            continue

        ans = candidate

    print(ans)


if __name__ == "__main__":
    main()
