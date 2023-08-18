# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    t = 0.0

    for ai, bi in ab:
        t += ai / bi

    t_half = t / 2

    t1 = 0
    ans = 0

    for ai, bi in ab:
        delta = ai / bi

        if t1 + delta <= t_half:
            t1 += delta
            ans += ai
        else:
            ans += (t_half - t1) * bi
            break

    print(ans)


if __name__ == "__main__":
    main()
