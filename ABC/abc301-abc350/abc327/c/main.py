# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    size = 9
    a = [list(map(int, input().split())) for _ in range(size)]

    for ai in a:
        if len(set(ai)) != 9:
            print("No")
            exit()

    for j in range(size):
        s = set()

        for i in range(size):
            s.add(a[i][j])

        if len(s) != 9:
            print("No")
            exit()

    for i in range(3):
        x, y, z = set(), set(), set()

        for j in range(3):
            x1, x2, x3 = a[3 * i + j][:3]
            y1, y2, y3 = a[3 * i + j][3:6]
            z1, z2, z3 = a[3 * i + j][6:]
            x.add(x1)
            x.add(x2)
            x.add(x3)
            y.add(y1)
            y.add(y2)
            y.add(y3)
            z.add(z1)
            z.add(z2)
            z.add(z3)

        if len(x) != 9 or len(y) != 9 or len(z) != 9:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
