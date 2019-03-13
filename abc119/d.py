# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_right

    a, b, q = map(int, input().split())
    s = [-float('inf')] + [int(input()) for _ in range(a)] + [float('inf')]
    t = [-float('inf')] + [int(input()) for _ in range(b)] + [float('inf')]

    # See:
    # https://img.atcoder.jp/abc119/editorial.pdf
    for _ in range(q):
        x = int(input())
        s_right = bisect_right(s, x)
        s_left = s_right - 1
        t_right = bisect_right(t, x)
        t_left = t_right - 1
        ans = float('inf')

        for si in [s[s_left], s[s_right]]:
            for ti in [t[t_left], t[t_right]]:
                ans = min(ans, abs(si - x) + abs(si - ti), abs(ti - x) + abs(si - ti))

        print(ans)


if __name__ == '__main__':
    main()
