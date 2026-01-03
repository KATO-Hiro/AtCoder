# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    a_count, b_count = 0, 0

    for i, si in enumerate(s):
        a_count += si == "A"
        b_count += si == "B"

        if i == 0:
            continue

        if a_count >= b_count:
            print("Alice")
        else:
            print("Bob")


if __name__ == "__main__":
    main()
