# -*- coding: utf-8 -*-


def main():
    n = int(input())
    y = list()

    for i in range(n):
        xi, li = map(int, input().split())
        # y.append((xi - li + 1, xi + li - 1))
        y.append((xi - li, xi + li))

    count = 1
    sorted_y = sorted(y, key=lambda x: x[1])
    end_point = sorted_y[0][1]

    for left, right in sorted_y[1:]:
        if left >= end_point:
            end_point = right
            count += 1

    print(count)


if __name__ == '__main__':
    main()
