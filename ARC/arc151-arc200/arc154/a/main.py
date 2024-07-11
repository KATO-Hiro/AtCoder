# -*- coding: utf-8 -*-


def main():
    import sys

    sys.set_int_max_str_digits(0)

    input = sys.stdin.readline

    n = int(input())
    a = list(input().rstrip())
    b = list(input().rstrip())

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]

    mod = 998244353
    a = int("".join(a)) % mod
    b = int("".join(b)) % mod
    ans = a * b % mod
    print(ans)


if __name__ == "__main__":
    main()
