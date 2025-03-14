# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    b = [i for i in range(1, 6)]
    a = list(map(int, input().split()))

    for i in range(4):
        c = b.copy()
        c[i], c[i + 1] = c[i + 1], c[i]

        if c == a:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
