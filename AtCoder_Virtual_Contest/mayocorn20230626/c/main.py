# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    c = [list(map(int, input().split())) for _ in range(3)]

    for a1 in range(101):
        for a2 in range(101):
            for a3 in range(101):
                a = [a1, a2, a3]
                bs = list()

                for i in range(3):
                    b = list()

                    for j in range(3):
                        b.append(c[i][j] - a[i])

                    bs.append(b)

                if bs[0] == bs[1] == bs[2]:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
