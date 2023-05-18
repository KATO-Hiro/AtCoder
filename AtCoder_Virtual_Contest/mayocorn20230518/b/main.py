# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    t = sum([ai / bi for ai, bi in ab])
    t_half = t / 2
    ans = 0

    for ai, bi in ab:
        t_dash = ai / bi

        if t_half > t_dash:
            ans += ai
            t_half -= t_dash
        else:
            ans += t_half * bi
            break

    print(ans)


if __name__ == "__main__":
    main()
