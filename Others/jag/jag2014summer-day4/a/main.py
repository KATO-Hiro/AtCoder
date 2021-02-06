# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    for t in range(a + b):
        value = 60 * t + c

        if value % (a + b) <= a:
            print(value)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
