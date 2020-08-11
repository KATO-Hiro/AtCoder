# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = 0
    ans += max(0, n * (n - 1) // 2)
    ans += max(0, m * (m - 1) // 2)

    print(ans)


if __name__ == '__main__':
    main()
