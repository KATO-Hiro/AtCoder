# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    lower = 1
    upper = 10 ** 18

    def f(g):
        return b * (g - 1) + a / pow(g, 0.5)


    while lower + 2 < upper:
        left_center = (2 * lower + upper) // 3
        right_center = (lower + 2 * upper) // 3

        if f(left_center) > f(right_center):
            lower = left_center
        else:
            upper = right_center

    ans = float("inf")
    
    for i in range(max(1, int(lower - 5)), int(upper) + 5):
        ans = min(ans, f(i))
    
    print(ans)
    

if __name__ == "__main__":
    main()
