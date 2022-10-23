# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    grid_max = 10 ** 4

    a = list(map(int, input().split()))
    ax = list()
    ay = list()

    for i, ai in enumerate(a):
        if i % 2 == 0:
            ax.append(ai)
        else:
            ay.append(ai)
    
    pattern_x = product([-1, 1], repeat=len(ax) - 1)
    pattern_y = product([-1, 1], repeat=len(ay))
    dp_x = set()
    dp_y = set()

    for i, pattern in enumerate(pattern_x):
        cand = 0

        for axi, flag in zip(ax, [1] + list(pattern)):
            cand += axi * flag
        
        dp_x.add(cand)
    
    for i, pattern in enumerate(pattern_y):
        cand = 0

        for ayi, flag in zip(ay, pattern):
            cand += ayi * flag
        
        dp_y.add(cand)

    if x in dp_x and y in dp_y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
