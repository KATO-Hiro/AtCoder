# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    mod = 998244353

    for i, patten in enumerate(product([0, 1], repeat=n)):
        if i == 0:
            continue

        a_max, b_sum = 0, 0

        for j, pi in enumerate(patten):
            if pi == 1:
                a_max = max(a_max, a[j])
                b_sum += b[j]

        if a_max >= b_sum:
            ans += 1

    print(ans % mod)


if __name__ == "__main__":
    main()
