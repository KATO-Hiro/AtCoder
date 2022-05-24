# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if s[0] == s[1]:
        print("Bad")
    elif s[1] == s[2]:
        print("Bad")
    elif s[2] == s[3]:
        print("Bad")
    else:
        print("Good")
    


if __name__ == "__main__":
    main()
