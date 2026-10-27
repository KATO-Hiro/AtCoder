# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = a + a
    acc = list(accumulate(b, initial=0))
    inf = 10**18
    ans = -inf

    for i in range(m, 2 * n + 1):
        candidate = acc[i] - acc[i - m]
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
