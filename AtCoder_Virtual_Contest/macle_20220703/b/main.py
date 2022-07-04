# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    if m == 0:
        print(1)
        exit()
    elif n == m:
        print(0)
        exit()

    a = list(map(int, input().split()))
    b = [0] + sorted(a) + [n + 1]
    diffs = list()

    for first, second in zip(b, b[1:]):
        diff = second - first - 1

        if diff > 0:
            diffs.append(diff)
    
    diff_min = min(diffs)
    ans = 0

    for d in diffs:
        ans += ceil(d / diff_min)

    print(ans)


if __name__ == "__main__":
    main()
