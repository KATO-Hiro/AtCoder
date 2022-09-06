# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, reverse=True)[:3]
    ans = 0

    for i, j, k in permutations(b):
        candidate = str(i) + str(j) + str(k)
        ans = max(ans, int(candidate))
    
    print(ans)


if __name__ == "__main__":
    main()
