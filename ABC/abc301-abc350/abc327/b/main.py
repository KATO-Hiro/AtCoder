# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    b = int(input())

    for a in range(1, 17):
        if a**a == b:
            print(a)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
