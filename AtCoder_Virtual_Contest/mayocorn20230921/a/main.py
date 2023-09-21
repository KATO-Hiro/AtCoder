# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    costs = list()

    for _ in range(n):
        ci, ti = map(int, input().split())

        if ti <= t:
            costs.append(ci)

    if len(costs) == 0:
        print("TLE")
    else:
        print(min(costs))


if __name__ == "__main__":
    main()
