# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, a, b, c = map(int, input().split())
    d = x / a + c
    e = x / b

    if d < e:
        print("Hare")
    elif d > e:
        print("Tortoise")
    else:
        print("Tie")


if __name__ == "__main__":
    main()
