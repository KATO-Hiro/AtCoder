# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = input().rstrip().split()
    a, b = int(a), int(b.replace(".", ""))
    print(a * b // 100)


if __name__ == "__main__":
    main()
