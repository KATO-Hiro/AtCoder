# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = "".join(sorted(s))

    if t == "ABC":
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
