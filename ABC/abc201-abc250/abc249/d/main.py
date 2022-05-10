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
    from collections import Counter, defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    size = 2 * 10 ** 5 + 10
    d = defaultdict(list)

    for i in range(1, size + 1):
        divisors = make_divisors(i)
        d[i] = divisors
    
    ans = 0

    for ai in a:
        for dai in d[ai]:
            ans += c[dai] * c[ai // dai]

    print(ans)


if __name__ == "__main__":
    main()
