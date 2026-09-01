# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = [(ai, i) for i, ai in enumerate(a, 1)]

    while len(b) > 1:
        m = len(b)
        c = []

        for i in range(m // 2):
            b1, b2 = b[2 * i], b[2 * i + 1]

            if b1[0] > b2[0]:
                c.append(b1)
            else:
                c.append(b2)

        b = c

    print(b[0][1])


if __name__ == "__main__":
    main()
