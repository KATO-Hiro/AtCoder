# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    k = int(input())
    cd = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

    patterns = product(*cd)
    ans = 0

    for pattern in patterns:
        pattern = set(pattern)

        count = 0

        for ai, bi in ab:
            if ai in pattern and bi in pattern:
                count += 1

        ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
