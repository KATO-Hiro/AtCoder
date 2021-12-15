# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s1 = input().rstrip()
    s2 = input().rstrip()
    count = s1.count("#") + s2.count("#")

    if count == 2 and s1[0] == s2[1] and s1[1] == s2[0]:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
