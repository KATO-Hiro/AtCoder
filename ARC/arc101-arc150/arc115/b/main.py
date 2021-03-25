# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = [list(map(int, input().split())) for _ in range(n)]
    a = list()
    b = list()

    for i in range(n):
        value_min = float("inf")

        for j in range(n):
            value_min = min(value_min, c[j][i])

        b.append(value_min)

    for j in range(n):
        diff = list()

        for i in range(n):
            diff.append(c[j][i] - b[i])

        if len(set(diff)) != 1:
            print("No")
            exit()

        a.append(diff[0])

    print("Yes")
    print(*a)
    print(*b)


if __name__ == "__main__":
    main()
