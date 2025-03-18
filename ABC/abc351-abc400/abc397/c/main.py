# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    first = Counter([a[0]])
    second = Counter(a[1:])
    left, right = len(first.keys()), len(second.keys())
    ans = left + right

    for i in range(1, n - 1):
        ai = a[i]

        if first[ai] == 0:
            left += 1

        first[ai] += 1
        second[ai] -= 1

        if second[ai] == 0:
            right -= 1

        ans = max(ans, left + right)

    print(ans)


if __name__ == "__main__":
    main()
