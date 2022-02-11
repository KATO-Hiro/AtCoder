# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    ans = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j <= s:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
