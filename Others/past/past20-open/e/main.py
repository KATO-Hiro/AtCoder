# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a, initial=0))
    ans = 0

    for left in range(1, n + 1):
        right = left + w - 1

        if right > n:
            break

        candidate = acc[right] - acc[left - 1]
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
