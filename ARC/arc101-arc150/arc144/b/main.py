# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    left, right = min(a), max(a)

    def f(candidate: int) -> bool:
        x_count, y_count = 0, 0

        for ai in a:
            if ai < candidate:
                x_count += ceil(candidate - ai, x)
            elif ai > candidate:
                y_count += (ai - candidate) // y

        return x_count <= y_count

    while abs(right - left) > 1:
        mid = (left + right) // 2

        if f(mid):
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
