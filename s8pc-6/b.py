# -*- coding: utf-8 -*-


def main():
    from statistics import median, median_high, median_low

    n = int(input())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]

    for i in range(n):
        ai, bi = map(int, input().split())
        a[i] = ai
        b[i] = bi

    ans = float('inf')

    for entrance in [median_low(a), median_high(a)]:
        for exporting in [median_low(b), median_high(b)]:
            entrance, exporting = median_low(a), median_low(b)
            entrance, exporting = median_high(a), median_high(b)
            count = (exporting - entrance) * n

            for ai, bi in zip(a, b):
                if bi <= exporting:
                    if ai >= entrance:
                        pass
                    else:
                        count += 2 * (entrance - ai)
                else:
                    if ai >= entrance:
                        count += 2 * (bi - exporting)
                    else:
                        count += 2 * (entrance - ai)
                        count += 2 * (bi - exporting)

            ans = min(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
