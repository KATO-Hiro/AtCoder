# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, large_c = map(int, input().split())
    c_count = large_c.bit_count()
    common = a + b - c_count

    if common % 2 == 1 or common < 0:
        print(-1)
        exit()

    common //= 2
    x, y = 0, 0
    a -= common
    b -= common

    for bit in range(60):
        if (large_c >> bit) & 1:
            if a > 0:
                x |= 1 << bit
                a -= 1
            elif b > 0:
                y |= 1 << bit
                b -= 1
        else:
            if common >= 1:
                x |= 1 << bit
                y |= 1 << bit
                common -= 1

    if (a != 0) or (b != 0) or (common != 0):
        print(-1)
        exit()
    else:
        print(x, y)


if __name__ == "__main__":
    main()
