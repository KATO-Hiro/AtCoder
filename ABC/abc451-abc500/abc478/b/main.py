# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n, v = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    ans = 0

    for i, j, k in permutations(range(1, n + 1), 3):
        if i + j + k > v:
            continue

        ans = max(ans, w[i] + w[j] + w[k])

    print(ans)


if __name__ == "__main__":
    main()
