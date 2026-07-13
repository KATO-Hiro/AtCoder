# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    t = list(map(int, input().split()))
    h2 = [0] * (n + 100)

    for _ in range(m):
        li, ri, wi = map(int, input().split())
        li -= 1
        h2[li] += wi
        h2[ri] -= wi

    h2 = list(accumulate(h2))
    ans = 0

    for hi, h2_i, ti in zip(h, h2, t):
        if (hi + h2_i) >= ti:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
