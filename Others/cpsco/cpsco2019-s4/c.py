# -*- coding: utf-8 -*-


def main():
    from bisect import bisect

    n, d = map(int, input().split())
    r = sorted(list(map(int, input().split())))
    ans = 0

    for i in range(n):
        min_r = r[i]
        max_r = min_r + d
        pos = bisect(r, max_r)
        diff = max(pos - i - 1, 0)
        ans += diff * (diff - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
