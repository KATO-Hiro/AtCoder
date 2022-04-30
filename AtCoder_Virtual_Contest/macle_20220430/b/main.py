# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    free_color_count = 0
    flag = False

    for ai in a:
        if ai >= 3200:
            free_color_count += 1
            flag = True
        else:
            p, q = divmod(ai, 400)
            d[p] = 1
    
    ans = len(d.keys())

    ans_min = ans
    ans_max = ans + free_color_count

    if ans == 0 and flag:
        ans_min += 1

    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
