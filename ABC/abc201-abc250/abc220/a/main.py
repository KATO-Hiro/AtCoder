# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    for i in range(a, b + 1):
        if i % c == 0:
            print(i)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
