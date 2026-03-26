# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    s = s.replace("a", "A")
    s = s.replace("e", "E")
    s = s.replace("i", "I")
    s = s.replace("o", "O")
    s = s.replace("u", "U")
    print(s)


if __name__ == "__main__":
    main()
