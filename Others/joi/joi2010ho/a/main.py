# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [int(input()) for _ in range(n - 1)]
    a = [int(input()) for _ in range(m)]
    t = list(accumulate(s, initial=0))
    # print(t)

    prev = 1
    ans = 0
    mod = 10**5

    for ai in a:
        cur = prev + ai
        # print(prev, cur)
        ans += abs(t[cur - 1] - t[prev - 1])
        ans %= mod

        prev = cur

    print(ans)


if __name__ == "__main__":
    main()
