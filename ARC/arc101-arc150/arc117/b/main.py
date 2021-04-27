# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + sorted(list(map(int, input().split())))
    mod = 10 ** 9 + 7
    ans = 1

    for first, second in zip(a, a[1:]):
        ans *= second - first + 1
        ans %= mod

    print(ans % mod)


if __name__ == "__main__":
    main()
