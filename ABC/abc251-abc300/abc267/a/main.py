# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][::-1]
    s = input().rstrip()
    print(days.index(s) + 1)


if __name__ == "__main__":
    main()
