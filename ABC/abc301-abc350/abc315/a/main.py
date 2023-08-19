# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    s = (
        s.replace("a", "")
        .replace("e", "")
        .replace("i", "")
        .replace("o", "")
        .replace("u", "")
    )
    print(s)


if __name__ == "__main__":
    main()
