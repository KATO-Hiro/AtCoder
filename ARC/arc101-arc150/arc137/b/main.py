# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    total_min, total_max = 0, 0
    lower, upper = 0, 0

    for ai in a:
        if ai == 0:
            total += 1
            total_max = max(total_max, total)
        else:
            total -= 1
            total_min = min(total_min, total)

        upper = max(upper, total - total_min)
        lower = min(lower, total - total_max)

    ans = upper - lower + 1
    print(ans)


if __name__ == "__main__":
    main()
