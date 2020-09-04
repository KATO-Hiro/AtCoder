# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys
    input = sys.stdin.readline

    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    ans = float('inf')

    for i, j, k in list(permutations([a1, a2, a3])):
        dist = abs(i - b1)
        dist += abs(j - b2)
        dist += abs(k - b3)

        ans = min(ans, dist)

    print(ans)


if __name__ == '__main__':
    main()
