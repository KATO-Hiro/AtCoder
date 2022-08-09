# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, w = map(int, input().split())
    w *= 1000

    inf = float('inf')
    ans_min = inf
    ans_max = -inf

    for n in range(1, 10 ** 6 + 1):
        if a * n <= w <= b * n:
            ans_min = min(ans_min, n)
            ans_max = max(ans_max, n)
    
    if ans_min == inf:
        print("UNSATISFIABLE")
    else:
        print(ans_min, ans_max)


if __name__ == "__main__":
    main()
