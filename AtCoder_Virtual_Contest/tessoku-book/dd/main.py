# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = n // 3 + n // 5 + n // 7
    ans -= n // (3 * 5)
    ans -= n // (5 * 7)
    ans -= n // (7 * 3)
    ans += n // (3 * 5 * 7)
    print(ans)


if __name__ == "__main__":
    main()
