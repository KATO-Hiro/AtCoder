# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())

    for _ in range(h):
        si = input().rstrip()

        if si.count("o") == 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
