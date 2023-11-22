# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import combinations

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for pattern in combinations(a, k):
        # print(pattern)
        ans += sum(pattern)

    print(ans)


if __name__ == "__main__":
    main()
