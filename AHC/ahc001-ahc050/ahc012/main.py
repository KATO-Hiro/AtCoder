# -*- coding: utf-8 -*-


def generate_points(value_min, value_max, count):
    from random import sample

    return sample(range(value_min, value_max), count)


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    points = generate_points(-10 ** 4, 10 ** 4, k * 4)
    tmp = list()

    # print(k)
    count = int(k * 0.95)
    print(count)

    while points:
        p = points.pop()
        tmp.append(p)

        if count > 0 and len(tmp) == 4:
            print(*tmp)
            tmp = list()
            count -= 1


if __name__ == "__main__":
    main()
