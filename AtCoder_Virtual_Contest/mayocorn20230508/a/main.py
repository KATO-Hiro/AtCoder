# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, k = map(int, input().split())
    ans = 0

    for key, count in [(1, a), (0, b), (-1, c)]:
        tmp = min(k, count)
        ans += tmp * key
        k -= tmp

        if k == 0:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
