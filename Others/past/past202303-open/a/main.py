# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, t = map(int, input().split())

    if s == 0:
        if t == 0:
            if n % 2 == 0:
                print("Bob")
            else:
                print("Alice")
        else:
            if n % 2 == 0:
                print("Alice")
            else:
                print("Bob")
    else:
        if t == 0:
            if n % 2 == 0:
                print("Alice")
            else:
                print("Bob")
        else:
            if n % 2 == 0:
                print("Bob")
            else:
                print("Alice")


if __name__ == "__main__":
    main()
