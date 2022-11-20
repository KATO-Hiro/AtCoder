# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    summed_t = sum(t)
    m = int(input())

    for i in range(m):
        pi, xi = map(int, input().split())
        pi -= 1

        print(summed_t - (t[pi] - xi))


if __name__ == "__main__":
    main()
