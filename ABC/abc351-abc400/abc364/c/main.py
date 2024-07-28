# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    count_a, count_b = 0, 0
    summed_a, summed_b = 0, 0

    for ai in a:
        count_a += 1
        summed_a += ai

        if summed_a > x:
            break

    for bi in b:
        count_b += 1
        summed_b += bi

        if summed_b > y:
            break

    ans = min(count_a, count_b)
    print(ans)


if __name__ == "__main__":
    main()
