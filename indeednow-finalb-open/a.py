# -*- coding: utf-8 -*-


def main():
    a = int(input())
    b = int(input())
    mod = 10 ** 9 + 7
    ans = 0

    # See:
    # https://beta.atcoder.jp/contests/indeednow-finalb-open/submissions/2066213
    for i in range(a, b + 1):
        ans += ((i ** 2 * (i + 1)) // 2) % mod

    print(ans % mod)


if __name__ == '__main__':
    main()
