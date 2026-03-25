# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    candidates = defaultdict(list)
    left, right = 0, n

    for i in range(n - 1):
        left += 1
        right -= 1

        if a[i] == a[i + 1]:
            continue

        diff = abs(right - left)
        candidates[diff].append(a[i + 1])

    key_min = min(candidates.keys())
    ans = max(candidates[key_min])
    print(ans)


if __name__ == "__main__":
    main()
