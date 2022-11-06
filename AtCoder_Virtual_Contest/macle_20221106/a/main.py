# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    ans = float("inf")

    for i, j, k in permutations(a, 3):
        ans = min(ans, abs(j - i) + abs(k - j))
    
    print(ans)


if __name__ == "__main__":
    main()
