# -*- coding: utf-8 -*-


def run_prime_factorization(max_number: int):
    from math import sqrt

    ans = dict()
    remain = max_number

    for j in range(2, int(sqrt(max_number)) + 1):
        if remain % j == 0:
            count = 0

            while remain % j == 0:
                count += 1
                remain //= j

            ans[j] = count

    if remain != 1:
        ans[remain] = 1

    return ans


def main():
    n, p = map(int, input().split())
    ans = 1

    # See:
    # https://www.youtube.com/watch?v=z0bIhkaSXY4
    results = run_prime_factorization(p)

    for base, exponent in results.items():
        ans *= base ** (exponent // n)

    print(ans)


if __name__ == '__main__':
    main()
