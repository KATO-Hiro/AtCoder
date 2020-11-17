# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    t = [list(map(int, input().split())) for _ in range(n)]

    patterns = list(permutations(range(1, n)))

    ans = 0

    for pattern in patterns:
        pattern = [0] + list(pattern) + [0]
        total = 0

        for first, second in zip(pattern, pattern[1:]):
            total += t[first][second]

        if total == k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
