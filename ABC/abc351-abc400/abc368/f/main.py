# -*- coding: utf-8 -*-


def run_prime_factorization(max_number: int) -> dict:
    from math import sqrt

    ans = dict()
    remain = max_number

    for base in range(2, int(sqrt(max_number)) + 1):
        if remain % base == 0:
            exponent_count = 0

            while remain % base == 0:
                exponent_count += 1
                remain //= base

            ans[base] = exponent_count

    if remain != 1:
        ans[remain] = 1

    return ans


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = []

    # Nimによる勝敗判定の問題に帰着
    for ai in a:
        ps = run_prime_factorization(ai)
        count = sum(ps.values())
        b.append(count)

    # print(b)
    result = 0

    for bi in b:
        result ^= bi

    if result != 0:
        print("Anna")
    else:
        print("Bruno")


if __name__ == "__main__":
    main()
