# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = n // 3
    ans += n // 5
    ans -= n // 15
    print(ans)


if __name__ == "__main__":
    main()
