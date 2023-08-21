# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 10**9 + 7
    # 全体 - (0のみない) - (9のみない) + (0と9ともにない)
    ans = pow(10, n, mod)
    ans -= 2 * pow(9, n, mod)
    ans += pow(8, n, mod)
    print(ans % mod)


if __name__ == "__main__":
    main()
