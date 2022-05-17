# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    c = Counter(s)
    size = len(set(s))

    if size == 2 and 2 in c.values():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
