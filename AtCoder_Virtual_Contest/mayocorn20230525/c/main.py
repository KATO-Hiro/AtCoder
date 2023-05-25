# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [tuple(map(int, input().split())) for _ in range(k)]
    ans = 0

    for pattern in product([0, 1], repeat=k):
        tmp = set()
        candidate = 0

        for i, pi in enumerate(pattern):
            tmp.add(cd[i][pi])

        for ai, bi in ab:
            if ai in tmp and bi in tmp:
                candidate += 1

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
