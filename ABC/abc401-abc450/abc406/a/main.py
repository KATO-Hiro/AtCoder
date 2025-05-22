# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    deadline = 60 * a + b
    submit = 60 * c + d

    if submit < deadline:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
