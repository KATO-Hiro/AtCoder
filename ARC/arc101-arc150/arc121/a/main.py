# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = list()

    for i in range(n):
        xi, yi = map(int, input().split())
        xy.append((xi, yi, i))

    sorted_by_x = sorted(xy, key=lambda x: x[0])
    sorted_by_y = sorted(xy, key=lambda x: x[1])

    ans = list()

    ans.append(
        (
            abs(sorted_by_x[0][0] - sorted_by_x[-2][0]),
            sorted_by_x[0][2],
            sorted_by_x[-2][2],
        )
    )
    ans.append(
        (
            abs(sorted_by_x[1][0] - sorted_by_x[-1][0]),
            sorted_by_x[1][2],
            sorted_by_x[-1][2],
        )
    )
    ans.append(
        (
            abs(sorted_by_y[0][1] - sorted_by_y[-2][1]),
            sorted_by_y[0][2],
            sorted_by_y[-2][2],
        )
    )
    ans.append(
        (
            abs(sorted_by_y[1][1] - sorted_by_y[-1][1]),
            sorted_by_y[1][2],
            sorted_by_y[-1][2],
        )
    )
    ans.append(
        (
            abs(sorted_by_x[0][0] - sorted_by_x[-1][0]),
            sorted_by_x[0][2],
            sorted_by_x[-1][2],
        )
    )
    ans.append(
        (
            abs(sorted_by_y[0][1] - sorted_by_y[-1][1]),
            sorted_by_y[0][2],
            sorted_by_y[-1][2],
        )
    )

    ans = sorted(ans, reverse=True)
    _, i1, j1 = ans[0]

    for value, i2, j2 in ans[1:]:
        if i1 != i2 or j1 != j2:
            print(value)
            exit()


if __name__ == "__main__":
    main()
