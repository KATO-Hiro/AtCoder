# -*- coding: utf-8 -*-


def f(a, b, g):
    return b * (g - 1) + a / pow(g, 0.5)


def main():
    from decimal import Decimal
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    lower = 1
    upper = 10 ** 36 + 10
    count = 500

    while count > 0:
        left_center = (2 * lower + upper) / 3
        right_center = (lower + 2 * upper) / 3

        if f(a, b, left_center) > f(a, b, right_center):
            lower = left_center
        else:
            upper = right_center

        count -= 1
    
    ans = list()
    
    for i in range(max(1, int(lower) - 3), int(lower) + 4):
        ans.append(Decimal("{:.10f}".format(f(a, b, i))))
    
    print(min(ans))
    

if __name__ == "__main__":
    main()
