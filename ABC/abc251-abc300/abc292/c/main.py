# -*- coding: utf-8 -*-


def run_prime_factorization(max_number: int) -> int:
    from math import sqrt

    ans = 1
    remain = max_number

    for base in range(2, int(sqrt(max_number)) + 1):
        if remain % base == 0:
            exponent_count = 0

            while remain % base == 0:
                exponent_count += 1
                remain //= base

            ans *= exponent_count + 1

    if remain != 1:
        ans *= 2

    return ans


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(int)
    ans = 0

    for i in range(1, n + 1):
        result = run_prime_factorization(i)
        d[i] = result
    
    for ab in range(1, n):
        cd = n - ab
        ans += d[ab] * d[cd]
    
    print(ans)
    

if __name__ == "__main__":
    main()
