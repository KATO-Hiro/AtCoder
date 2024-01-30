# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    for i, si in enumerate(s, 1):
        if i == 1:
            if si.islower():
                print("No")
                exit()
        else:
            if si.isupper():
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
