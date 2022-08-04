# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    cd = [tuple(map(int, input().split())) for _ in range(m)]

    for ai, bi in ab:
        cost_min, index = float("inf"), -1

        for j, (cj, dj) in enumerate(cd, 1):
            cost = abs(cj - ai) + abs(dj - bi)

            if cost < cost_min:
                cost_min = cost
                index = j
        
        print(index)


if __name__ == "__main__":
    main()
