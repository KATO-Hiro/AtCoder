# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    x = defaultdict(int)
    y = defaultdict(int)

    for i in range(3):
        xi, yi = map(int, input().split())
        x[xi] += 1
        y[yi] += 1

    ans_x, ans_y = 0, 0

    for key, xi in x.items():
        if xi == 1:
            ans_x = key

    for key, yi in y.items():
        if yi == 1:
            ans_y = key
    
    print(ans_x, ans_y)


if __name__ == "__main__":
    main()
