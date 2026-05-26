# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a, initial=0))
    candidates = []

    for left in range(1, n + 1):
        for right in range(left, n + 1):
            if right - left + 1 > k:
                continue

            candidate = acc[right] - acc[left - 1]
            candidates.append(candidate)

    candidates.sort(reverse=True)
    ans = sum(candidates[:m])
    print(ans)


if __name__ == "__main__":
    main()
