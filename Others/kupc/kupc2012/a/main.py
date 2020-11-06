# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t, e = map(int, input().split())
    x = list(map(int, input().split()))

    t_min = t - e
    t_max = t + e

    for ti in range(t_min, t_max + 1):
        for index, xi in enumerate(x, 1):
            if ti % xi == 0:
                print(index)
                exit()

    print(-1)


if __name__ == "__main__":
    main()
