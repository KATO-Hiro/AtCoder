# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))

    ans = 0

    for pattern in permutations(range(1, n + 1)):
        candidate = list(pattern)

        if p < candidate < q:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
