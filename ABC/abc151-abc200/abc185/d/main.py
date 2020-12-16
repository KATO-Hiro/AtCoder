# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    if m == 0:
        print(1)
        exit()

    if n == m:
        print(0)
        exit()

    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)

    if max_a != n:
        a.append(n + 1)

    if min_a != 1:
        a.append(0)

    sorted_a = sorted(a)
    diff = list()

    for first, second in zip(sorted_a, sorted_a[1:]):
        d = second - first - 1

        if d > 0:
            diff.append(d)

    diff_min = min(diff)
    ans = 0

    for di in diff:
        p, q = divmod(di, diff_min)
        ans += p

        if q != 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
