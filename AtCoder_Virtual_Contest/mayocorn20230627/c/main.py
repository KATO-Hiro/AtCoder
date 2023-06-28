# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    cd = set(tuple(map(int, input().split())) for _ in range(m))

    for pattern in permutations(range(1, n + 1)):
        count = 0

        for i, j in ab:
            pi, pj = pattern[i - 1], pattern[j - 1]

            if (pi, pj) in cd or (pj, pi) in cd:
                count += 1

        if count == m:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
