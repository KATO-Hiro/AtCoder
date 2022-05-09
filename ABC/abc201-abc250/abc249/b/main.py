# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = [ord(si) - ord('A') for si in s]

    if len(s) != len(set(t)):
        print("No")
    elif s == s.lower() or s == s.upper():
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
