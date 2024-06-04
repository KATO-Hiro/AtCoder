# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    ans = [i for i in range(1, n + 1)]
    ans[l - 1 : r] = ans[l - 1 : r][::-1]
    print(*ans)


if __name__ == "__main__":
    main()
