# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    digit = len(str(n))
    mod = 998244353
    minus = 0
    ans = 0

    for i in range(digit):
        value_min = 10 ** i
        value_max = 10 ** (i + 1) - 1

        if n < value_min:
            break
        else:
            m = min(value_max, n) - minus
            ans += m *(m + 1) // 2
            ans %= mod

        minus *= 10
        minus += 9
    
    print(ans)


if __name__ == "__main__":
    main()
