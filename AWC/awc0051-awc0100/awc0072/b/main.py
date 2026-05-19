# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []

    for ai in a:
        if ai > 0:
            b.append(ai)
        else:
            b.append(0)

    acc = list(accumulate(b))
    base = sum(a[:k])
    ans = base + acc[-1] - acc[k - 1]

    for left in range(1, n):
        right = left + k - 1

        if right >= n:
            break

        base -= a[left - 1]
        base += a[right]
        candidate = base + acc[left - 1] + acc[-1] - acc[right]
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
