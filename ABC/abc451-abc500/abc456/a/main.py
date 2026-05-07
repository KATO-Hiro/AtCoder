# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    for i in range(1, 6 + 1):
        for j in range(1, 6 + 1):
            for k in range(1, 6 + 1):
                if (i + j + k) == x:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
