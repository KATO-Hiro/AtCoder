# -*- coding: utf-8 -*-


def main():
    import sys

    sys.set_int_max_str_digits(0)

    input = sys.stdin.readline

    s = input().rstrip().split("*")
    ans = 1
    mod = 998244353

    for si in s:
        ans *= int(si)
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
