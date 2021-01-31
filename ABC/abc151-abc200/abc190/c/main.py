# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    k = int(input())
    cd = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

    patterns = product([0, 1], repeat=k)
    ans = 0

    for pattern in patterns:
        dishes = [0 for _ in range(n)]

        for index, p in enumerate(pattern):
            pos = cd[index][p]
            dishes[pos] += 1

        count = 0

        for ai, bi in ab:
            if dishes[ai] >= 1 and dishes[bi] >= 1:
                count += 1

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
