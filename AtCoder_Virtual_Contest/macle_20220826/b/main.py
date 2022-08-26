# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    value_max = 2 * 10 ** 5 + 10
    imos = [0] * value_max

    for i in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri] -= 1
    
    imos = list(accumulate(imos))
    is_started = False
    ans = list()

    for i, im in enumerate(imos):
        if im >= 1 and not is_started:
            is_started = True
            ans.append(i)
        elif im == 0 and is_started:
            is_started = False
            ans.append(i)
    
    for i in range(len(ans) // 2):
        print(ans[2 * i], ans[2 * i + 1])


if __name__ == "__main__":
    main()
