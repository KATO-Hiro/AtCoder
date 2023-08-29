# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    colors = [0] * 9

    for ai in a:
        p, q = divmod(ai, 400)

        if p >= 8:
            colors[8] += 1
        else:
            colors[p] += 1

    # print(colors)

    count = sum([1 for color in colors[:-1] if color >= 1])
    # print(count)
    count_min = count

    if count_min == 0:
        count_min += 1

    count_max = count + colors[8]

    print(count_min, count_max)


if __name__ == "__main__":
    main()
