# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0
    best_pattern = []

    for pattern in permutations(range(n)):
        candidate = 0

        for i, pi in enumerate(pattern):
            ai, bi = ab[pi]

            if i == n - 1:
                candidate += bi
            else:
                candidate += ai

        if candidate > ans:
            ans = candidate
            best_pattern = pattern

    print(ans)
    print(best_pattern)


if __name__ == "__main__":
    main()
