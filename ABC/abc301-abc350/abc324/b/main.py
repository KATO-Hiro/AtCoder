# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    upper = 61

    for x in range(upper):
        x2 = 2**x

        if x2 > n:
            break

        for y in range(upper):
            y3 = 3**y

            if x2 * y3 == n:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
