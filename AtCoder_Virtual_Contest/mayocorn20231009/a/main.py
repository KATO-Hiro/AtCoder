# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    v, a, b, c = map(int, input().split())
    remain = v

    while True:
        if remain < a:
            print("F")
            break

        remain -= a

        if remain < b:
            print("M")
            break

        remain -= b

        if remain < c:
            print("T")
            break

        remain -= c


if __name__ == "__main__":
    main()
