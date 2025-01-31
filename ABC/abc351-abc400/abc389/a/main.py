# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    s = s.replace("x", "*")
    print(eval(s))


if __name__ == "__main__":
    main()
