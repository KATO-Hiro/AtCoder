# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    xyz = list(map(int, input().split()))
    print(xyz[2], xyz[0], xyz[1])


if __name__ == "__main__":
    main()
