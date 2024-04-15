# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)
    d = Counter(c.values())

    for value in d.values():
        if not (value == 0 or value == 2):
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
