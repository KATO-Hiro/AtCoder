# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    w_count = [0 for _ in range(n)]
    b_count = [0 for _ in range(n)]
    r_count = [0 for _ in range(n)]

    for index, si in enumerate(s):
        w_count[index] = si.count('W')
        b_count[index] = si.count('B')
        r_count[index] = si.count('R')

    w_count = list(accumulate([0] + w_count))
    b_count = list(accumulate([0] + b_count))
    r_count = list(accumulate([0] + r_count))

    ans = float('inf')

    for i in range(1, n):
        for j in range(i + 1, n):
            k = n - j

            if k <= 0:
                continue

            count = b_count[i] + r_count[i]
            count += (w_count[j] - w_count[i]) + (r_count[j] - r_count[i])
            count += (w_count[n] - w_count[j]) + (b_count[n] - b_count[j])

            ans = min(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
