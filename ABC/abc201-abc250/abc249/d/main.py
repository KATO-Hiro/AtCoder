# -*- coding: utf-8 -*-


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1

    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)

            if i != n // i:
                upper_divisors.append(n//i)

        i += 1

    return lower_divisors + upper_divisors[::-1]


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for ai in a:
        d = make_divisors(ai)

        for di in d:
            ans += c[di] * c[ai // di]

    print(ans)


if __name__ == "__main__":
    main()
