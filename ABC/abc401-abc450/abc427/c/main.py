# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    uv = [tuple(map(int, input().split())) for _ in range(m)]
    inf = 10**18
    ans = inf

    for bit in range(1 << n):
        candidate = 0

        for ui, vi in uv:
            if ((bit >> ui) & 1) == ((bit >> vi) & 1):
                candidate += 1

        ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
