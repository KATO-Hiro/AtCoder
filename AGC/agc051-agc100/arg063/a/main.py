# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    a_count, b_count = 0, 0

    if s[0] == "A":
        a_count += 1
    else:
        b_count += 1

    for i, si in enumerate(s[1:], 1):
        if si == "A":
            a_count += 1
        else:
            b_count += 1

        if i % 2 == 1:
            b_count -= 1

            if b_count <= 0:
                print("Alice")
            else:
                print("Bob")
        else:
            a_count -= 1

            if a_count <= 0:
                print("Bob")
            else:
                print("Alice")


if __name__ == "__main__":
    main()
