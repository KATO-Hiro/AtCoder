# -*- coding: utf-8 -*-


def main():
    n = int(input())
    h = [int(input()) for _ in range(n)]
    diff = [h[i + 1] - h[i] for i in range(n - 1)]
    plus_minus = list()

    if diff[0] < 0:
        plus_minus.append(0)

    plus_count = 0
    minus_count = 0
    j = 0

    while j < n - 1:
        if diff[j] < 0:
            if plus_count > 0:
                plus_minus.append(plus_count)
                plus_count = 0

            minus_count += 1
        else:
            if minus_count > 0:
                plus_minus.append(minus_count)
                minus_count = 0

            plus_count += 1

        j += 1

    if minus_count > 0:
        plus_minus.append(minus_count)

    if plus_count > 0:
        plus_minus.append(plus_count)
        plus_minus.append(0)

    m = len(plus_minus)
    ans = 0

    for k in range(m - 1):
        ans = max(ans, plus_minus[k] + plus_minus[k + 1])

    print(ans + 1)


if __name__ == '__main__':
    main()
