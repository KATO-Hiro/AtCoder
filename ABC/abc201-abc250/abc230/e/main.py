# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n = int(input())
    numbers = set()

    for i in range(1, int(sqrt(n)) + 1):
        m1 = n // i
        m2 = n // m1

        numbers.add((m1, i))
        numbers.add((m2, m1))
    
    k = sorted((numbers), reverse=True)
    ans = n

    for k1, k2 in zip(k, k[1:]):
        count = k2[1] - k1[1]
        value = k2[0]
        ans += count * value
    
    print(ans)


if __name__ == "__main__":
    main()
