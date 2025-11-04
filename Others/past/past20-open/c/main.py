# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    s1, s2, s3 = s.split("X")
    print(s1 + s2[::-1] + s3)


if __name__ == "__main__":
    main()
