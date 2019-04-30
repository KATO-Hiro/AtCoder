# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())

    if b >= 1:
        ds = sorted(list(map(int, input().split())))
        min_ds = min(ds)
        max_ds = max(ds)
        ans = n - b

        for i in range(1, len(ds)):
            if ds[i] - ds[i - 1] > a:
                ans -= 1

        if min_ds - 1 >= a:
            ans -= 1
        if n - max_ds >= a:
            ans -= 1
        if a == 1:
            ans = 0

        print(ans)
    else:
        from math import ceil
        print(n - ceil(n / a))


if __name__ == '__main__':
    main()
