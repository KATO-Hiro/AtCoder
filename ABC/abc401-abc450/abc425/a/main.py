# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    for i in range(1, n + 1):
        ans += ((-1) ** i) * (i**3)

    print(ans)


if __name__ == "__main__":
    main()
