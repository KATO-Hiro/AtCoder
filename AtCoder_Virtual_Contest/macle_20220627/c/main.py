# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    mod = 10 ** 9 + 7
    ans = 1

    if n % 2 == 0:
        for i in range(n // 2):
            m = 2 * i + 1

            if c[m] == 2:
                ans *= 2
            else:
                ans *= 0
            
            ans %= mod
    else:
        for i in range(n // 2 + 1):
            m = 2 * i

            if m == 0:
                pass
            elif c[m] == 2:
                ans *= 2
            else:
                ans *= 0

            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
