# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    ab, bc, ca = map(int, input().split())
    print(ab * bc // 2)


if __name__ == "__main__":
    main()
